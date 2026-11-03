"""基本結構檢查；不代表醫療查核或專業審閱。Python 3，無外部套件。"""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
index = (root / 'wiki/index.md').read_text(encoding='utf-8')
required = ['title', 'type', 'status', 'created', 'updated', 'reviewed_by', 'reviewed_at', 'source_ids', 'tags']
for path in root.rglob('*.md'):
    if 'raw' in path.relative_to(root).parts:
        continue
    text = path.read_text(encoding='utf-8')
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
        if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
            continue
        target = target.split('#')[0]
        if target and not (path.parent / target).exists():
            errors.append(f'{path.relative_to(root)}: 無效連結 {target}')
    if path.parent.name not in ['sources', 'topics', 'concepts', 'qa', 'syntheses'] or 'wiki' not in path.relative_to(root).parts:
        continue
    front = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not front:
        errors.append(f'{path.name}: 缺少 frontmatter')
        continue
    fields = dict(re.findall(r'^(\w+):\s*([^\n]*)', front[1], re.M))
    for key in required:
        if key not in fields:
            errors.append(f'{path.name}: 缺少 {key}')
    if fields.get('status') not in ['draft', 'needs-review', 'reviewed', 'archived']:
        errors.append(f'{path.name}: 狀態不合法')
    if fields.get('status') == 'reviewed':
        for key in ['reviewed_by', 'reviewed_at']:
            if fields.get(key, '').strip() in ['', 'null', '~', '""', "''"]:
                errors.append(f'{path.name}: reviewed 缺少 {key}')
        if fields.get('source_ids', '[]').strip() == '[]':
            errors.append(f'{path.name}: reviewed 缺少來源')
    relative = path.relative_to(root / 'wiki').as_posix()
    if f']({relative})' not in index:
        errors.append(f'{path.name}: 未列入索引')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('PASS：本地連結、知識頁必要欄位、索引與基本審閱欄位檢查通過。仍需查核來源與內容。')

import os
import re
from pathlib import Path
import subprocess

def get_git_date(filepath):
    try:
        # Get last commit date for the file
        result = subprocess.run(['git', 'log', '-1', '--format=%cd', '--date=short', str(filepath)], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def fix_updated():
    exp_dir = Path('wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments')
    autofixed = []
    
    for exp_file in exp_dir.glob('*.md'):
        content = exp_file.read_text()
        git_date = get_git_date(exp_file)
        
        if not git_date: continue
        
        updated_match = re.search(r'^updated:\s*(.*)$', content, re.MULTILINE)
        if updated_match:
            updated_val = updated_match.group(1).strip()
            # Try to extract just the date part if it has quotes or other formatting
            date_match = re.search(r'\d{4}-\d{2}-\d{2}', updated_val)
            if date_match:
                updated_date = date_match.group(0)
                if updated_date != git_date and git_date > updated_date:
                    # Replace the updated field
                    new_content = re.sub(r'^updated:.*$', f"updated: {git_date}", content, flags=re.MULTILINE)
                    exp_file.write_text(new_content)
                    autofixed.append(f"Updated {exp_file.name} date from {updated_date} to {git_date}")

    print(f"Fixed {len(autofixed)} updated dates:")
    for f in autofixed:
        print(f)

if __name__ == '__main__':
    fix_updated()

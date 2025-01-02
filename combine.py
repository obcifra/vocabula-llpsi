import os
from pathlib import Path

def combine_files(directory: Path) -> None:
    """
    Combine all files in a directory into a single file.
    Ignores '#' comments in the files.
    """
    with open('combined.txt', 'w') as combined_file:
        for filename in os.listdir(directory):
            with open(directory / filename, encoding='utf-8-sig') as file:
                for line in file:
                    if not line.startswith('#'):
                        if not ':' in line:
                            print(f'Invalid line: {line} in {filename}')
                            exit
                        combined_file.write(line)

if __name__ == '__main__':
    combine_files(Path('vocabula'))

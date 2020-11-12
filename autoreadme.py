import glob

all_q = set(glob.glob('q/*.q'))
euler = set(f'q/{i + 1}.q' for i in range(750))
count = len(all_q & euler)

readme = "# Project Euler Solutions in kdb-q\n\n"

readme += "Problem | Solution | Input\n --- | --- | ---\n"

with open('names.txt', 'r') as f:
    names = f.readlines()

for i in range(1, count + 1):
    readme += f'[{names[i - 1].rstrip()}](https://projecteuler.net/problem={i}) | '
    readme += f'[{i}.q](q/{i}.q) | '
    readme += f'[input](q/inputs/{i}.txt)\n'

with open('README.md', 'w') as f:
    f.write(readme)


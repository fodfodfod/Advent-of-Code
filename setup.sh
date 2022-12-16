d=$(date +%d)

d=$1
cookie=$(head -n 1 cookiefile)

mkdir "day $d"

cd "day $d"

echo -e "file = open(\"day $d/input.txt\", \"r\")\nraw_string = file.read()\nfile.close()" > "challenge 1.py"

curl "https://adventofcode.com/2022/day/$d/input" -b "session=$cookie" | tac | tac > input.txt

cd ..

code .

firefox "https://adventofcode.com/2022/day/$d"
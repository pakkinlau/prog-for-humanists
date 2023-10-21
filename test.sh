max_changes=0
most_changed_file=""

for commit_hash in $(git log --pretty=format:'%H' -- '*.txt'); do
    changes=$(git diff --shortstat $commit_hash | grep -E '([0-9]+) insertions\(\+\), ([0-9]+) deletions\(-\)' | awk '{print $1+$4}')
    if ((changes > max_changes)); then
        max_changes=$changes
        most_changed_file=$(git diff --name-only $commit_hash^..$commit_hash)
    fi
done

echo "Most changed file: $most_changed_file"
echo "Number of changes: $max_changes"

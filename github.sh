# De;ete all `.ipynb_checkpoints` folders
find . -name .ipynb_checkpoints -type d -exec rm -rf {} \;

git add --all && git commit -m "Update" && git push

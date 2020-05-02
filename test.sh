echo "Code Compile and Test"
WD=$(PWD)/$2/$1
if [$1 -eq "CPP"]
then
    echo "===============compilation================"
    g++ -g $WD/main.cpp -o $WD/main.out
    echo "==================Running=================="
    cat $2/input.txt | $WD/$2/$1/main.out > $WD/test.txt
else
    cd $WD
    cat ../input.txt | python main.py > test.txt
    cd ../..
fi

echo "==================Testing=================="
diff $WD/test.txt $2/output.txt > $WD/final
[-s $WD/final] && (echo "fail"; exit 0) || echo "pass"
echo "==================output diff==============="
cat final
echo "==================git upload ============="
git commit -m "Code Updation"
echo "==================original git diff=================="
git diff $(git rev-parse --abbrev-ref HEAD)..master | cat 
echo "==================Git PUSH==========================="
git push --set-upstream origin

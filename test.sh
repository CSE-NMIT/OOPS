echo "Code Compile and Test"
WD="$(pwd)/Assignments/$2/$1"
assignment="$(pwd)/Assignments/$2"
if ["$1" -eq "CPP"]
then
    echo "===============compilation================"
    g++ -g $WD/main.cpp -o $WD/main.out
    echo "==================Running=================="
    cat $assignment/input.txt | $WD/main.out > $WD/test.txt
else
    cd $WD
    cat ../input.txt | python3 main.py > test.txt
    cd ../..
fi

echo "==================Testing=================="
diff $WD/test.txt $assignment/output.txt > $WD/final
if [[ -f "$WD/final" ]]
then
    if [[-s "$WD/final" ]]
    then
        echo "fail"; exit 0
    else
        echo "pass"
    fi
else
    exit 0
fi
echo "==================output diff==============="
cat $WD/final
echo "==================git upload ============="
git commit -m "Code Updation"
echo "==================original git diff=================="
git diff $(git rev-parse --abbrev-ref HEAD)..master | cat 
echo "==================Git PUSH==========================="
git push --set-upstream origin

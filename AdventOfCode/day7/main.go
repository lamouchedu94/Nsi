package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type folder []string

func main() {
	data, err := read("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(data)
    run(data)
}

func run(tab []folder) int{
	var nums []int
	// /var tab_num []num
	var temp string 

    for _, t := range tab {
		for _,num :=range t {
			temp = ""
			for _,car:= range num {
				if car >='0' && car <= '9'{
					temp=temp+string(car)
				}else {
					break
				}
				
			}
	n, _:= strconv.Atoi(temp)
	nums = append(nums, n)
	fmt.Println(nums)
		}
		//fmt.Println(t)
	}
return 0
}

func read(path string) ([]folder, error) {
	var tab []folder
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)
	
	var f folder
	for test.Scan() {
		data := test.Text()
		//var f folder


			//fmt.Println(string(data[0]))
			if int(data[0]) >= '1' && int(data[0]) <= '9' {
				f = append(f, data)
				//fmt.Println(data)

			}

		if data[0] == '$' {
			//fmt.Println()
			if len(f) > 0 {
				tab = append(tab, f)
				f = folder{}

			}
			

		}

	}
	if len(f)>0{
		tab = append(tab, f)
		f = folder{}
	}
	return tab, err

}


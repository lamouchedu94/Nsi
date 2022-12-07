package main

import (
	"bufio"
	"fmt"
	"os"
)

type folder []string

func main() {
	data, err := read("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(data)

}

func run(tab []folder) int{

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


package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	tab, _ := read("input.txt")
	//fmt.Println(temp[0])
	//fmt.Printf("%s and %s", tab[0], tab[1])
	fmt.Println(run(tab))
}

// [2 4]
// [6 8]

// [3 7]
// [2 8]

func run(tab []string) int {
	var res int
	for i := 0; i < len(tab); i += 2 {
		grp1 := strings.Split(tab[i], "-")
		grp2 := strings.Split(tab[i+1], "-")

		if (grp1[0] <= grp2[0] && grp1[1] >= grp2[1]) || (grp2[0] <= grp1[0] && grp2[1] >= grp1[1]) {
			res += 1
		}

		//fmt.Println("\n", grp1, grp2)
	}

	return res
}

func read(path string) ([]string, error) {
	var tab []string
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)

	for test.Scan() {
		valsplit := strings.Split(test.Text(), ",")
		tab = append(tab, valsplit...)

	}
	return tab, err
}

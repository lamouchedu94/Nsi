package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	tab, _ := read("input1.txt")
	//fmt.Println(temp[0])
	//fmt.Printf("%s and %s", tab[0], tab[1])
	fmt.Println(run1(tab))
	fmt.Println(run2(tab))
}

// [2 4]
// [6 8]

// [3 7]
// [2 8]

type team struct {
	a, b, c, d int
}

func run2(tab []team) int {
	var res int

	for _, t := range tab {
		if (t.a <= t.c && t.c <= t.b) || (t.c <= t.a && t.a <= t.d) {
			res += 1
		}

		//fmt.Println("\n", grp1, grp2)
	}

	return res
}

func run1(tab []team) int {
	var res int

	for _, t := range tab {
		if (t.a <= t.c && t.d <= t.b) || (t.c <= t.a && t.b <= t.d) {
			res += 1
		}

		//fmt.Println("\n", grp1, grp2)
	}

	return res
}

func read(path string) ([]team, error) {
	var tab []team
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)

	for test.Scan() {
		var t team

		fmt.Sscanf(test.Text(), "%d-%d,%d-%d", &t.a, &t.b, &t.c, &t.d)
		tab = append(tab, t)
	}
	return tab, err
}

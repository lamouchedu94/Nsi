package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	tab, err := read("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(tab[1])
	//fmt.Println(tab[0])
}

type instruct struct {
	a, b, c int
}

func decoupage(line string, tab []string) []string {
	if string(line[1]) != " " {
		tab[0] += string(line[1])
	} else {
		tab[0] += " "
	}
	if string(line[5]) != " " {
		tab[1] += string(line[5])
	} else {
		tab[1] += " "
	}
	if string(line[9]) != " " {
		tab[2] += string(line[9])
	} else {
		tab[2] += " "
	}
	return tab
}
func read(path string) ([]string, error) {
	var tab []string
	var tabinstruction []instruct
	fin := true

	//var colonne []string
	for i := 0; i < 3; i++ {
		temp := []string{""}
		tab = append(tab, temp...)
	}

	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)

	for test.Scan() {
		if test.Text() == " 1   2   3 " {
			fin = false

		}
		if fin {
			tab = decoupage(test.Text(), tab)
			tab = append(tab, test.Text())
		} else {

			var ins instruct
			fmt.Sscanf(test.Text(), "move %d from %d to %d", &ins.a, &ins.b, &ins.c)
			tabinstruction = append(tabinstruction, ins)
		}

	}
	return tab, err
}

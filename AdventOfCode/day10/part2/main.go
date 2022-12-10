package main

import (
	"bufio"
	"fmt"
	"os"
)

type instructs struct {
	inst   string
	number int
}

func main() {
	a, err := read("../input1.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	//fmt.Println(a[0].number)
	_, tab := run(a)
	print(tab)

}

func print(tab []int) {

	for ligne := 0; ligne < 6; ligne++ {
		for colone := 0; colone < 40; colone++ {
			cycle := ligne*40 + colone
			x := tab[cycle]
			if x-1 <= colone && colone <= x+1 {
				fmt.Print("#")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println()
	}
}

func run(ins []instructs) (int, []int) {
	x := 1
	var total []int

	for _, ins := range ins {
		switch ins.inst {
		case "noop":
			total = append(total, x)
		case "addx":
			total = append(total, x)
			total = append(total, x)
			x += ins.number
		}

	}
	total = append(total, x)
	sum := 0
	for _, p := range []int{20, 60, 100, 140, 180, 220} {
		sum += total[p-1] * p
	}
	return sum, total
}

func read(path string) ([]instructs, error) {
	var tab []instructs
	file, err := os.Open(path)
	if err != nil {
		file.Close()
		return nil, err
	}

	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)

	for test.Scan() {
		var ins instructs
		fmt.Sscanf(test.Text(), "%s %d", &ins.inst, &ins.number)
		tab = append(tab, ins)
	}
	return tab, err

}

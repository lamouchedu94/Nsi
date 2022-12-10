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
	fmt.Println(run(a))
}

func run(ins []instructs) int {
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
	sum := 0
	for _, p := range []int{20, 60, 100, 140, 180, 220} {
		sum += total[p-1] * p
	}
	return sum
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

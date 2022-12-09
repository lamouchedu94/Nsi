package main

import (
	"bufio"
	"fmt"
	"os"
)

type instructs struct {
	direction string
	rep       int
}

func main() {
	fmt.Println(read("input.txt"))
}

func read(path string) ([]instructs, error) {
	var tab []instructs
	file, err := os.Open(path)
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)

	for test.Scan() {
		var ins instructs
		fmt.Sscanf(test.Text(), "%s %d", &ins.direction, &ins.rep)
		tab = append(tab, ins)
	}
	return tab, err

}

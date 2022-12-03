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
		return
	}
	calc(tab)
}

func calc(tab []string) {
	var sep int
	for _, car := range tab {
		sep = len(car) / 2

		for i := 0; i < sep; i++ {
			for j := sep; j < len(car); j++ {
				if car[i] == car[j] {
					fmt.Println(string(car[i]), car[j])
				}
			}
		}
		break
	}

}

func read(path string) ([]string, error) {
	var tab []string
	file, err := os.Open(path)
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)

	for test.Scan() {
		tab = append(tab, test.Text())
	}
	return tab, err
}

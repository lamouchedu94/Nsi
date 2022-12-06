package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	a, _ := read("input.txt")

	fmt.Println(a)
	run(a)
}

func run(text []byte) {
	for pas := 0; pas < len(text); pas++ {
		ifdiff := true
		if pas < 14 {
			continue
		}
	out:
		for i := pas - 14; i < pas; i++ {
			for j := pas - 14; j < pas; j++ {
				fmt.Println(i, j, text[i], text[j])
				if text[j] == text[i] && i != j {
					ifdiff = false
					break out
				}
			}
		}
		if ifdiff {
			fmt.Println("Trouve a", pas)
			return
		}

	}

	//fmt.Println(string(temp))
}

func read(path string) ([]byte, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)
	test.Scan()
	return test.Bytes(), err

}

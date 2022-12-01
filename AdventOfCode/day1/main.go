package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	tab, err := read("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	//fmt.Println(tab)
	//fmt.Println(calc(tab))
	temp := calc(tab)
	fmt.Println(len(temp))
	max := findMaxElement(temp)
	fmt.Printf("La valeur maximale est : %d", max)
}

func findMaxElement(arr []int) int {
	max_num := arr[0]
	for i := 0; i < len(arr); i++ {
		if arr[i] > max_num {
			max_num = arr[i]
		}
	}
	return max_num
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

func calc(tab []string) []int {
	var res []int
	var val int
	var err error
	var temp int
	for i, car := range tab {
		if car != "" {
			val, err = strconv.Atoi(car)
			temp += val
			if err != nil {
				return res
			}
		} else {
			res = append(res, temp)
			if temp == 82055 {
				fmt.Println(i)
			}
			temp, val = 0, 0

		}

	}

	return res
}

func read1(path string) ([]int, error) {
	var rep []int
	var n []int
	file, err := os.Open(path)
	if err != nil {
		return rep, err
	}
	test := bufio.NewScanner(file)
	test.Split(bufio.ScanLines)
	for test.Scan() {
		test, _ := strconv.ParseInt(test.Text(), 6, 12)
		n = append(rep, int(test))

	}
	return n, err
}

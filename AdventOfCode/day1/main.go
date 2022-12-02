package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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
	sort.Ints(temp)

	sum := 0
	for i := 1; i <= 3; i++ {
		sum += temp[len(temp)-i]
	}
	//exo 1
	max := MaxElement(temp)
	fmt.Printf("La valeur maximale est : %d", max)
	fmt.Println()
	//exo 2
	fmt.Printf("Le nb de calories de 3 luttins est : %d", sum)
}

func MaxElement(tab []int) int {
	max_num := tab[0]
	for i := 0; i < len(tab); i++ {
		if tab[i] > max_num {
			max_num = tab[i]
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
	for _, car := range tab {
		if car != "" {
			val, err = strconv.Atoi(car)
			temp += val
			if err != nil {
				return res
			}
		} else {
			res = append(res, temp)
			temp, val = 0, 0

		}

	}

	return res
}

/*
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
*/

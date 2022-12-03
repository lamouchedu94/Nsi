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
	fmt.Println("Partie 1 :", part1(tab))
	fmt.Println("Partie 2 :", part2(tab))
	//A = 65
	//a = 97
}

func part2(tab []string) int {
	//var sep int
	var res int
	for i := 0; i < len(tab); i += 3 {
	out:
		for j := 0; j < len(tab[i]); j++ {
			for k := 0; k < len(tab[i+1]); k++ {
				for l := 0; l < len(tab[i+2]); l++ {
					if tab[i][j] == tab[i+1][k] && tab[i][j] == tab[i+2][l] {
						if 65 <= int(tab[i][j]) && int(tab[i][j]) <= 90 {
							res += int(tab[i][j]) - 38
						} else {
							res += int(tab[i][j]) - 96
						}
						break out
						//fmt.Println(tab[i][j])
					}
				}
			}
		}
	}
	return res
}

func part1(tab []string) int {
	var sep int
	var res int
	for _, car := range tab {
		sep = len(car) / 2
	out:
		for i := 0; i < sep; i++ {
			for j := sep; j < len(car); j++ {
				if car[i] == car[j] {
					if 65 <= int(car[i]) && int(car[i]) <= 90 {
						res += int(car[i]) - 38
					} else {
						res += int(car[i]) - 96
					}
					break out
				}

			}
		}

	}
	return res
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

/*
vJrwpWtwJgWr 	 hcsFMMfFFhFp
jqHRNqRjqzjGDLGL rsFMfFZSrLrFZsSL
PmmdzqPrV		 vPwwTWBwg
*/

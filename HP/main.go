package main

import (
	"fmt"
	"time"
)

func main() {

	l1 := make([]int, 10000)
	l2 := make([]int, 10000)
	for i := 0; i < 10000; i++ {
		l1[i] = i
	}
	i := 10000
	for j := 0; j < 10000; j++ {
		l2[j] = i
		i++
	}

	//l1 := []int{2, 5, 7, 13, 64}
	//l2 := []int{1, 3, 4, 11, 35, 52, 58, 61}
	deb := time.Now()
	for i := 0; i < 3000; i++ {
		fusion(l1, l2)
		//fmt.Println(fusion(l1, l2))
	}
	fmt.Println(time.Since(deb))
	//fmt.Println(time.Now().Sub(deb))
}

func fusion(l1 []int, l2 []int) []int {
	res := make([]int, len(l1)+len(l2))
	curs1 := 0
	curs2 := 0
	for curs1 < len(l1) && curs2 < len(l2) {
		if l1[curs1] < l2[curs2] {
			res[curs1+curs2] = l1[curs1]
			curs1 += 1
		} else {
			res[curs1+curs2] = l2[curs2]
			curs2 += 1
		}
	}
	if curs1 == len(l1) && curs2 < len(l2) {
		for i := curs2; i < len(l2); i++ {
			res[curs1+curs2] = l2[curs2]
			curs1 += 1
		}
	} else {
		for i := curs1; i < len(l1); i++ {
			res[curs1+curs2] = l1[curs1]
			curs1 += 1
		}
	}

	return res
}

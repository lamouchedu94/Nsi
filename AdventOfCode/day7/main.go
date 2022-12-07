package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

type directory struct {
	name      string
	fileSize  int
	totalSize int
	parent    *directory
	subdirs   []*directory
}

func main() {
	data, err := read("input1.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	calc(data)
	//print(data)
	r := 0
	res(data, &r)
	//fmt.Println(r)
	alib := 30000000 - (70000000 - data.totalSize)
	//fmt.Println(alib)
	var tab []int
	tabTotalSize(data, &tab)
	sort.Ints(tab)
	//fmt.Println(tab)
	fmt.Println(min(tab, alib))
}

func min(tab []int, alib int) int {
	for _, number := range tab {
		if number > alib {
			return number
		}
	}
	return 0
}

func tabTotalSize(d *directory, t *[]int) {
	for _, dir := range d.subdirs {
		*t = append(*t, d.totalSize)
		tabTotalSize(dir, t)
	}

}

func res(d *directory, total *int) {
	for _, dir := range d.subdirs {
		res(dir, total)
	}
	if d.totalSize <= 100000 {
		*total = *total + d.totalSize
	}

}

func calc(d *directory) int {

	d.totalSize = d.fileSize
	for _, dir := range d.subdirs {
		d.totalSize += calc(dir)
	}
	return d.totalSize
}

func read(path string) (*directory, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	test := bufio.NewScanner(file)

	root := directory{name: "/"}
	curdir := &root

	for test.Scan() {
		data := test.Text()

		switch {
		case strings.HasPrefix(data, "$ cd"):
			var a string
			fmt.Sscanf(data, "$ cd %s", &a)
			if a == "/" {
				continue
			}
			if a == ".." {
				curdir = curdir.parent
				continue
			}
			newdir := directory{name: a, parent: curdir}

			curdir.subdirs = append(curdir.subdirs, &newdir)
			curdir = &newdir

		case strings.HasPrefix(data, "dir"):
			continue

		case strings.HasPrefix(data, "$ ls"):
			continue

		default:
			var size int
			var name string
			fmt.Sscanf(data, "%d %s", &size, &name)
			curdir.fileSize += size
		}

	}

	return &root, err

}

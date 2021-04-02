package main

import "fmt"

func main() {
	initialNumbers := make([]int, 3)
	fmt.Println("digite uma sequencia de 3 numeros:")
	fmt.Scan(&initialNumbers)

	fmt.Println(initialNumbers[0])
}

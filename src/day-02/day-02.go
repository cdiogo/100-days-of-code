package main

import "fmt"

func main() {
	initialNumbers := getInitialNumbers()
	finalSlice := calculateTribonacci(initialNumbers)

	fmt.Println("The final sequence is \n", finalSlice)
}

func getInitialNumbers() []int {
	var initialNumbers []int

	fmt.Println("Hi,can you please digit 3 random numbers?")

	for i := 0; i <= 2; i++ {
		var receivedNumber int
		fmt.Printf("Please digit a number:")
		fmt.Scan(&receivedNumber)
		initialNumbers = append(initialNumbers, receivedNumber)
	}

	fmt.Println(initialNumbers)
	return initialNumbers
}

func calculateTribonacci(finalNumbers []int) []int {
	lenInitial := len(finalNumbers)
	var finalSliceLength int
	fmt.Printf("Tell how many positions you want to appear in the sequence: ")
	fmt.Scan(&finalSliceLength)
	positionsToAdd := finalSliceLength - lenInitial

	for i := 1; i <= positionsToAdd; i++ {
		lenFinal := len(finalNumbers)
		numberToAdd := finalNumbers[lenFinal-3] + finalNumbers[lenFinal-2] + finalNumbers[lenFinal-1]
		finalNumbers = append(finalNumbers, numberToAdd)
	}
	return finalNumbers
}

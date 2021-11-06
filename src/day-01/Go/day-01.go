package main

import (
	"fmt"
)

const daysInYear = 365

func main() {
	ageYears := receiveAgeInYears()
	ageDays := convertYearsInDays(ageYears)
	fmt.Println("calcAge(", ageYears, ")", "-> ", ageDays, "days")
}

func receiveAgeInYears() int {
	var ageInYears int
	fmt.Println("Hi, how old are you?")
	fmt.Scan(&ageInYears)

	return ageInYears
}

func convertYearsInDays(ageInYears int) int {
	var ageInDays int
	ageInDays = ageInYears * daysInYear
	return ageInDays
}

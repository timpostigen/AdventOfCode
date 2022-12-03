[CmdletBinding()]
param(
	$Type = "Python"
)

Push-Location

$name = "aoc-$((get-date).Year)"

if ($Type -eq "rust") {
	cargo new $name
} else {
	Set-Location $PSScriptRoot

	New-Item -Type Directory $PSScriptRoot/$name -Force
}

Copy-item aoc-base.code-workspace $name/"$name.code-workspace"

code $name/"$name.code-workspace"

Pop-Location

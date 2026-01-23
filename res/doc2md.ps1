<#
Converts all .docx files under this folder to markdown using pandoc.

Behavior:
- For each found .docx, determine its top-level folder relative to this script's folder.
- Create a sibling folder named <topfolder>.md next to the top-level folder (e.g. "4-04-04-02_3.md").
- Place converted .md files into that folder, preserving the relative path under the top-level folder.
- Generate `docx.md` in this folder with headings per top-level folder and links to both .docx and converted .md files.

Requirements: pandoc must be installed and available on PATH.
#>

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Script directory: $scriptDir"

if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Error "pandoc not found in PATH. Please install pandoc and ensure it's on PATH."
    exit 2
}

$docxFiles = Get-ChildItem -Path $scriptDir -Recurse -Filter *.docx -File -ErrorAction SilentlyContinue
if (-not $docxFiles -or $docxFiles.Count -eq 0) {
    Write-Host "No .docx files found under $scriptDir"
    exit 0
}

$groups = @{}

foreach ($f in $docxFiles) {
    $rel = $f.FullName.Substring($scriptDir.Length + 1).TrimStart('\')
    $parts = $rel -split '\\'

    if ($parts.Count -ge 2) {
        $top = $parts[0]
        $relativeUnderTop = ($parts[1..($parts.Count - 1)] -join '\\')
    } else {
        # docx sits directly under scriptDir
        $top = Split-Path $scriptDir -Leaf
        $relativeUnderTop = $parts[0]
    }

    $outTopDir = Join-Path $scriptDir ("$top.md")
    $outRelativePath = [System.IO.Path]::ChangeExtension($relativeUnderTop, '.md')
    $outFullPath = Join-Path $outTopDir $outRelativePath
    $outParent = Split-Path $outFullPath -Parent
    if (-not (Test-Path $outParent)) { New-Item -ItemType Directory -Force -Path $outParent | Out-Null }

    Write-Host "Converting: $rel -> $outFullPath"
    try {
        & pandoc -f docx -t gfm -o "$outFullPath" "$($f.FullName)"
    } catch {
        Write-Warning "pandoc failed for $($f.FullName): $_"
        continue
    }

    # prepare relative links used for index
    $docxRelLink = ($rel -replace '\\','/')
    $mdRelLink = (Join-Path "$top.md" $outRelativePath) -replace '\\','/'

    if (-not $groups.ContainsKey($top)) { $groups[$top] = @() }
    $groups[$top] += [PSCustomObject]@{ Docx = $docxRelLink; Md = $mdRelLink }
}

# Build the index file
$indexPath = Join-Path $scriptDir 'docx.md'
$lines = @()
$lines += "# Docx / Markdown index"
$lines += "Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$lines += ""

foreach ($top in ($groups.Keys | Sort-Object)) {
    $display = if ($top -eq (Split-Path $scriptDir -Leaf)) { "根目录" } else { $top }
    $lines += "## $display"
    $lines += ""
    foreach ($item in $groups[$top]) {
        $lines += "- [$($item.Docx)]($($item.Docx)) — [markdown]($($item.Md))"
    }
    $lines += ""
}

$lines -join "`n" | Set-Content -Path $indexPath -Encoding UTF8
Write-Host "Wrote index to $indexPath"

Write-Host "Done. Converted $($docxFiles.Count) docx files."

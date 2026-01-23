$files = Get-ChildItem "人工智能训练师三级考试平台模拟界面\*.html" | Sort-Object Name
$outputContent = @()
$navLinks = @()

foreach ($file in $files) {
    Write-Host "Processing $($file.Name)..."
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    $title = "Untitled"
    if ($content -match '(?ms)<title>(.*?)</title>') {
        $title = $matches[1].Trim()
    }

    # Generate a unique ID for the section based on filename
    $sectionId = "sec-" + ($file.BaseName -replace '\.', '-')

    if ($content -match '(?ms)<div class="container">(.*)</div>\s*</body>') {
        $examContent = $matches[0] -replace '\s*</body>', ''
    } else {
        if ($content -match '(?ms)<body>(.*)</body>') {
             $examContent = $matches[1]
        } else {
             $examContent = "<p>Error parsing content for $($file.Name)</p>"
        }
    }

    # Add to Navigation list
    $navLinks += "<li><a href='#$sectionId'>$title</a></li>"

    # Add to Content
    $outputContent += "<section id='$sectionId' class='exam-item'>"
    $outputContent += "<h2 class='exam-title'>$title</h2>"
    $outputContent += $examContent
    $outputContent += "</section>"
}

$css = @"
<style>
    :root {
        --primary-color: #0078e7;
        --bg-color: #f4f6f9;
        --nav-width: 280px;
        --header-height: 60px; /* Approx height of the blue title bar */
    }

    * { box-sizing: border-box; }

    body {
        font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        background-color: var(--bg-color);
        color: #333;
        margin: 0;
        padding: 0;
        line-height: 1.6;
        display: flex;
        height: 100vh;
        overflow: hidden; /* Prevent body scroll, we scroll main instead */
    }

    /* --- Sidebar Navigation --- */
    nav.side-nav {
        width: var(--nav-width);
        height: 100vh;
        background: #2c3e50;
        color: white;
        display: flex;
        flex-direction: column;
        border-right: 1px solid #1a252f;
        flex-shrink: 0;
    }

    nav.side-nav h2 {
        padding: 20px;
        margin: 0;
        font-size: 1.1em;
        background: #1a252f;
        color: #ecf0f1;
        text-align: center;
        flex-shrink: 0;
    }

    nav.side-nav ul {
        list-style: none;
        padding: 0;
        margin: 0;
        overflow-y: auto; /* Scrollable nav */
        flex: 1;
    }

    nav.side-nav ul li a {
        display: block;
        padding: 12px 20px;
        color: #bdc3c7;
        text-decoration: none;
        font-size: 0.9em;
        border-left: 4px solid transparent;
        transition: all 0.2s;
        border-bottom: 1px solid #34495e;
    }

    nav.side-nav ul li a:hover {
        background: #34495e;
        color: white;
        border-left-color: var(--primary-color);
    }

    /* --- Main Content Area --- */
    main.content {
        flex: 1;
        height: 100vh;
        overflow-y: scroll; /* Allow vertical scrolling between sections */
        scroll-snap-type: y mandatory; /* Snap to each question */
        scroll-behavior: smooth;
    }

    /* H1 Title at the very top (optional, scrolls away) */
    h1.main-title {
        text-align: center;
        color: #2c3e50;
        margin: 0;
        padding: 20px;
        background: #fff;
        border-bottom: 1px solid #eee;
        scroll-snap-align: start;
    }

    /* --- Exam Section --- */
    .exam-item {
        height: 100vh; /* Force full viewport height */
        display: flex;
        flex-direction: column;
        scroll-snap-align: start; /* Snap point */
        background: #fff;
        border-bottom: 1px solid #ddd;
        position: relative;
    }

    .exam-title {
        background: var(--primary-color);
        color: white;
        margin: 0;
        padding: 15px 25px;
        font-size: 1.3em;
        font-weight: 500;
        flex-shrink: 0; /* Title doesn't shrink */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        z-index: 10;
    }

    /* --- Flex Container for Columns --- */
    .container {
        flex: 1; /* Take up all remaining vertical space */
        display: flex;
        overflow: hidden; /* Crucial: contain the scrollbars inside */
        padding: 0;
        height: calc(100vh - 65px); /* Fallback/Safety */
    }

    .left-column, .right-column {
        height: 100%; /* Fill the container */
        overflow-y: auto; /* Independent scrolling */
        padding: 30px;
    }

    .left-column {
        flex: 6; /* 60% */
        border-right: 1px solid #e0e0e0;
        background: #fff;
    }

    .right-column {
        flex: 4; /* 40% */
        background: #fdfdfd;
    }

    /* Scrollbar styling for Webkit (Chrome/Edge/Safari) */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #f1f1f1; }
    ::-webkit-scrollbar-thumb { background: #ccc; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #bbb; }

    /* Typography inside content */
    h3 {
        color: #2c3e50;
        border-left: 4px solid var(--primary-color);
        padding-left: 10px;
        margin-top: 10px;
        margin-bottom: 15px;
        font-size: 1.1em;
    }

    p { margin-bottom: 1em; text-align: justify; }

    /* Buttons & Tables */
    .pure-button {
        display: inline-block;
        padding: 8px 16px;
        background: #e0e0e0;
        border: none;
        border-radius: 4px;
        color: #333;
        text-decoration: none;
        cursor: pointer;
        font-size: 0.9em;
        margin-right: 5px;
    }
    .pure-button-primary { background: var(--primary-color); color: white; }
    
    .pure-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        font-size: 0.9em;
    }
    .pure-table th, .pure-table td {
        padding: 10px;
        border-bottom: 1px solid #eee;
        text-align: left;
    }
    .pure-table th { background-color: #f8f9fa; }

    @media (max-width: 900px) {
        .container { flex-direction: column; }
        .left-column, .right-column { flex: none; height: 50%; width: 100%; }
        .left-column { border-right: none; border-bottom: 1px solid #eee; }
        nav.side-nav { display: none; } /* Hide nav on mobile or make it a drawer */
        main.content { margin-left: 0; }
    }
</style>
"@

$navHtml = @"
    <nav class="side-nav">
        <h2>试题导航</h2>
        <ul>
            $($navLinks -join "`n")
        </ul>
    </nav>
"@

$htmlHeader = @"
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>人工智能训练师三级上网</title>
    $css
</head>
<body>
    $navHtml
    <main class="content">
       
"@

$htmlFooter = @"
    </main>
</body>
</html>
"@

$finalHtml = $htmlHeader + ($outputContent -join "`n") + $htmlFooter
$finalHtml | Set-Content "ai_3_questions.html" -Encoding UTF8

Write-Host "Done! File saved to ai_3_questions.html"
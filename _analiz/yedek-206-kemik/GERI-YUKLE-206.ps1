# 206 kemik kataloğuna geri döner (56 adlandırılmış grup).
# Kullanım: Bu dosyaya sağ tık > "PowerShell ile çalıştır"
$base = "C:\Users\Berat\Desktop\KomiteninYeri"
$bk = Join-Path $base "_analiz\yedek-206-kemik"

Copy-Item (Join-Path $bk "Skeleton.tsx") "$base\sinav-platformu\src\pages\Skeleton.tsx" -Force

Write-Host "206 kemik kataloglu surum geri yuklendi." -ForegroundColor Green
Write-Host "Dev sunucusunu yeniden baslatmayi unutma: npm run dev" -ForegroundColor Yellow

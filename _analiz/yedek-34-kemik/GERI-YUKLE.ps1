# 34 kemikli iskelet sistemine geri döner.
# Kullanım: Bu dosyaya sağ tık > "PowerShell ile çalıştır"
$base = "C:\Users\Berat\Desktop\KomiteninYeri"
$bk = Join-Path $base "_analiz\yedek-34-kemik"

Copy-Item (Join-Path $bk "Skeleton.tsx") "$base\sinav-platformu\src\pages\Skeleton.tsx" -Force
Copy-Item (Join-Path $bk "skeleton-bones.obj") "$base\sinav-platformu\public\models\skeleton-bones.obj" -Force
Copy-Item (Join-Path $bk "split_skeleton.py") "$base\_analiz\split_skeleton.py" -Force

Write-Host "34 kemikli surum geri yuklendi." -ForegroundColor Green
Write-Host "Dev sunucusunu yeniden baslatmayi unutma: npm run dev" -ForegroundColor Yellow

# Q12 – Electricity Bill Calculation

**Question-paper requirements:** calculate bill from units, push code to GitHub, configure Jenkins build automation and create a Docker image.

## Illustrative lab tariff
- First 100 units: Rs. 2 per unit
- Next 100 units: Rs. 3 per unit
- Above 200 units: Rs. 5 per unit

For 250 units: 100×2 + 100×3 + 50×5 = Rs. 750.
These are example lab rates, not official electricity tariffs.

## A. Console program
```powershell
python electricity.py
```

## B. GitHub
Create an empty repository and push this folder using the general Git commands in the top-level README.

## C. Flask API (optional local verification)
```powershell
pip install -r requirements.txt
python app.py
```
Open `http://localhost:5000/bill?units=250`; expected JSON includes `"bill": 750`.

## D. Docker image
```powershell
docker build -t electricity-app .
docker run -d -p 5001:5000 --name electricity-container electricity-app
```
Test `http://localhost:5001/bill?units=250`.

Stop/remove:
```powershell
docker rm -f electricity-container
```

## E. Jenkins
The included Jenkinsfile is for a Windows Jenkins agent because it uses `bat` commands.

1. Push this folder's contents to its own GitHub repository (Dockerfile must be at repository root).
2. Jenkins → New Item → Pipeline.
3. Definition: **Pipeline script from SCM**.
4. SCM: Git; enter repository URL; Branch: `*/main`; Script Path: `Jenkinsfile`.
5. Save → Build Now.
6. Check Console Output; test `http://localhost:5001/bill?units=250`.

The Jenkins agent needs Docker CLI and Docker Engine access. Host port 5001 is used to avoid conflict with Q9's default port 5000 and Jenkins' usual web port 8080.

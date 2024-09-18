/*let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
*/

let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                const response = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = `
                    <p>Dominant Emotion: ${response.dominant_emotion}</p>
                    <pre>${JSON.stringify(response.emotions, null, 2)}</pre>
                `;
            } else {
                const errorResponse = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = `
                    <p>Error: ${errorResponse.error}</p>
                `;
            }
        }
    };
    xhttp.open("POST", "/analyze", true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ text: textToAnalyze }));
}

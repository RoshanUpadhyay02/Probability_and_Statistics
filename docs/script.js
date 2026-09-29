async function calculateMean() 
{
    // Getting input from the html file
    let input = document.getElementById("numbers").value;

    // Converting comma-separated values into a list
    let numbers = input.split(", ").map(Number);

    // Sending data to Python API
    let response = await fetch(
        "https://probability-and-statistics-1420.onrender.com/api/mean",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                numbers: numbers
            })
        }
    );

    let data = await response.json();

    // Display python result
    document.getElementById("result").innerText = "Mean = " + data.mean; 

}

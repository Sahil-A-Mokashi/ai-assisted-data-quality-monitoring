const API="http://127.0.0.1:5000";

window.onload=()=>{

loadDashboard();

loadDatasets();

}

async function loadDashboard(){

const response=await fetch(`${API}/dashboard`);

const data=await response.json();

document.getElementById("total-datasets").innerText=data.total_datasets;

document.getElementById("low-risk").innerText=data.low_risk;

document.getElementById("medium-risk").innerText=data.medium_risk;

document.getElementById("high-risk").innerText=data.high_risk;

document.getElementById("avg-quality").innerText=data.average_quality_score+"%";

}

async function loadDatasets(query=""){

const response=await fetch(`${API}/datasets${query}`);

const datasets=await response.json();

const body=document.getElementById("datasets-body");

body.innerHTML="";

datasets.forEach(dataset=>{

body.innerHTML+=`

<tr>

<td>${dataset.dataset_id}</td>

<td>${dataset.dataset_name}</td>

<td>${dataset.organisation}</td>

<td>${dataset.total_rows}</td>

<td>${dataset.total_columns}</td>

<td>${dataset.quality_score}</td>

<td>${dataset.predicted_risk}</td>

</tr>

`;

});

}

document.getElementById("apply").onclick=()=>{

const search=document.getElementById("search").value;

const risk=document.getElementById("risk").value;

const sort=document.getElementById("sort").value;

const order=document.getElementById("order").value;

let query="?";

if(search)

query+=`search=${search}&`;

if(risk)

query+=`predicted_risk=${risk}&`;

if(sort)

query+=`sort=${sort}&`;

query+=`order=${order}`;

loadDatasets(query);

}
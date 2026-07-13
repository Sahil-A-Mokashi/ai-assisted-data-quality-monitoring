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

<td>
    <a href="/dataset/${dataset.dataset_id}">
        ${dataset.dataset_name}
    </a>
</td>

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

if(document.getElementById("dataset-id")){

loadDatasetReport();

}

async function loadDatasetReport(){

const id=document.getElementById("dataset-id").value;

const response=await fetch(`${API}/reports/${id}`);

const report=await response.json();

const dataset=report.dataset;

const metrics=report.metrics;


document.getElementById("dataset-info").innerHTML=`

<p><strong>ID:</strong> ${dataset.dataset_id}</p>

<p><strong>Name:</strong> ${dataset.dataset_name}</p>

<p><strong>Organisation:</strong> ${dataset.organisation}</p>

<p><strong>Source:</strong> ${dataset.source_system}</p>

<p><strong>Domain:</strong> ${dataset.domain}</p>

<p><strong>Uploaded By:</strong> ${dataset.uploaded_by}</p>

<p><strong>Upload Date:</strong> ${dataset.upload_date}</p>

<p><strong>Status:</strong> ${dataset.status}</p>

`;

document.getElementById("quality-metrics").innerHTML=`

<p><strong>Total Rows:</strong> ${dataset.total_rows}</p>

<p><strong>Total Columns:</strong> ${dataset.total_columns}</p>

<p><strong>Missing Values:</strong> ${metrics.missing_values}</p>

<p><strong>Duplicate Rows:</strong> ${metrics.duplicate_rows}</p>

<p><strong>Null Percentage:</strong> ${metrics.null_percentage}%</p>

<p><strong>Completeness:</strong> ${metrics.completeness_score}%</p>

<p><strong>Consistency:</strong> ${metrics.consistency_score}%</p>

`;


document.getElementById("ai-analysis").innerHTML=`

<p><strong>Quality Score:</strong> ${dataset.quality_score}%</p>

<p><strong>Risk Level:</strong> ${dataset.predicted_risk}</p>

<p><strong>Anomaly Probability:</strong> ${metrics.anomaly_probability}%</p>

<p><strong>Status:</strong> ${metrics.anomaly_status}</p>

`;


document.getElementById("future-links").innerHTML=`

<p>

<strong>Generated Report:</strong>

${metrics.report_path ?? "Not generated"}

</p>

<p>

<strong>Corrected Dataset:</strong>

${metrics.corrected_dataset_path ?? "Not available"}

</p>

`;
}



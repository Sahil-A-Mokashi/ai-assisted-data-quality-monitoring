const API="http://127.0.0.1:5000";

window.onload = () => {

    // Dashboard page
    if (document.getElementById("dashboard-cards")) {

        loadDashboard();
        loadDatasets();

        const applyButton = document.getElementById("apply");

        if (applyButton) {
            applyButton.onclick = applyFilters;
        }

    }

    // Dataset details page
    if (document.getElementById("dataset-id")) {

        loadDatasetReport();

    }

};

async function loadDashboard(){

const response=await fetch(`${API}/dashboard`);

const data=await response.json();

document.getElementById("total-datasets").innerText=data.total_datasets;

document.getElementById("low-risk").innerText=data.low_risk;

document.getElementById("medium-risk").innerText=data.medium_risk;

document.getElementById("high-risk").innerText=data.high_risk;

document.getElementById("avg-quality").innerText=data.average_quality_score+"%";

}

async function loadDatasets(query = "") {

    const response = await fetch(`${API}/datasets${query}`);

    const datasets = await response.json();

    const body = document.getElementById("datasets-body");

    body.innerHTML = "";

    datasets.forEach(dataset => {

        let badge = "success";

        if (dataset.predicted_risk === "Medium")
            badge = "warning";

        if (dataset.predicted_risk === "High")
            badge = "danger";

        body.innerHTML += `
<tr>
    <td>#${dataset.dataset_id}</td>

    <td>
        <a href="/dataset/${dataset.dataset_id}">
            ${dataset.dataset_name}
        </a>
    </td>

    <td>${dataset.organisation}</td>

    <td>${dataset.total_rows}</td>

    <td>${dataset.total_columns}</td>

    <td style="min-width:180px;">
        <div class="progress">
            <div class="progress-bar bg-success"
                 style="width:${dataset.quality_score}%">
                ${dataset.quality_score}%
            </div>
        </div>
    </td>

    <td>
        <span class="badge bg-${badge}">
            ${dataset.predicted_risk}
        </span>
    </td>

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

const response = await fetch(`${API}/reports/${id}`);

if (response.status === 403) {

    alert("Please log in to view this private dataset.");

    window.location.href = "/login";

    return;

}

const report=await response.json();

const dataset=report.dataset;

const metrics=report.metrics;
createCharts(dataset, metrics);

document.getElementById("dataset-info").innerHTML=`

<p><strong>ID:</strong> #${dataset.dataset_id}</p>

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

function createCharts(dataset, metrics){

    // ----------------------------
    // Quality Score
    // ----------------------------

    document.getElementById("quality-score-value").innerHTML =
        `${dataset.quality_score}%`;

    new Chart(

        document.getElementById("quality-score-chart"),

        {

            type: "doughnut",

            data: {

                labels: ["Quality", "Remaining"],

                datasets: [{

                    data: [
                        dataset.quality_score,
                        100 - dataset.quality_score
                    ]

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: true,

                cutout: "70%",

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        }

    );



    // ----------------------------
    // Data Quality Breakdown
    // ----------------------------

    new Chart(

        document.getElementById("breakdown-chart"),

        {

            type: "doughnut",

            data: {

                labels: [

                    "Valid Rows",

                    "Missing Values",

                    "Duplicate Rows"

                ],

                datasets: [{

                    data: [

                        dataset.total_rows -
                        metrics.missing_values -
                        metrics.duplicate_rows,

                        metrics.missing_values,

                        metrics.duplicate_rows

                    ]

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: true,

                cutout: "55%",

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        }

    );



    // ----------------------------
    // Quality Metrics
    // ----------------------------

    document.getElementById("quality-bars").innerHTML = `

        <label class="fw-bold">Completeness</label>

        <div class="progress mb-3">

            <div class="progress-bar bg-success"
                 style="width:${metrics.completeness_score}%">

                ${metrics.completeness_score}%

            </div>

        </div>

        <label class="fw-bold">Consistency</label>

        <div class="progress mb-3">

            <div class="progress-bar bg-primary"
                 style="width:${metrics.consistency_score}%">

                ${metrics.consistency_score}%

            </div>

        </div>

        <label class="fw-bold">Null Percentage</label>

        <div class="progress">

            <div class="progress-bar bg-danger"
                 style="width:${metrics.null_percentage}%">

                ${metrics.null_percentage}%

            </div>

        </div>

    `;



    // ----------------------------
    // AI Risk Assessment
    // ----------------------------

    let badge = "success";

    if(dataset.predicted_risk === "Medium")
        badge = "warning";

    if(dataset.predicted_risk === "High")
        badge = "danger";

    document.getElementById("ai-summary").innerHTML = `

        <h5>Risk Level</h5>

        <span class="badge bg-${badge} fs-6">

            ${dataset.predicted_risk}

        </span>

        <hr>

        <h5>AI Confidence</h5>

        <div class="progress mb-3">

            <div class="progress-bar bg-info"
                 style="width:${metrics.anomaly_probability}%">

                ${metrics.anomaly_probability}%

            </div>

        </div>

        <h5>Status</h5>

        <span class="badge bg-success fs-6">

            Prediction Complete

        </span>

    `;

}
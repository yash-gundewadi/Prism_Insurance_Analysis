// Tab switching functionality
function switchTab(tabName) {
    // Hide all tab content
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    const selectedTab = document.getElementById(tabName + '-tab');
    if (selectedTab) {
        selectedTab.classList.add('active');
    }
    
    // Add active class to clicked button
    event.target.classList.add('active');
}

// File upload and analysis
document.addEventListener('DOMContentLoaded', function() {
    const uploadBtn = document.getElementById('uploadBtn');
    const fileInput = document.getElementById('fileInput');
    const resultsSection = document.getElementById('resultsSection');
    const resultsContent = document.getElementById('resultsContent');
    
    if (uploadBtn) {
        uploadBtn.addEventListener('click', handleFileUpload);
    }
    
    async function handleFileUpload() {
        const file = fileInput.files[0];
        
        if (!file) {
            alert('Please select a file first');
            return;
        }
        
        if (!file.name.endsWith('.csv')) {
            alert('Please select a CSV file');
            return;
        }
        
        uploadBtn.disabled = true;
        uploadBtn.textContent = 'Processing...';
        
        try {
            const formData = new FormData();
            formData.append('file', file);
            
            const response = await fetch('/api/analyze', {
                method: 'POST',
                body: formData
            });
            
            if (!response.ok) {
                throw new Error('Analysis failed: ' + response.statusText);
            }
            
            const result = await response.json();
            displayResults(result);
            
        } catch (error) {
            resultsContent.innerHTML = `<p style="color: red;"><strong>Error:</strong> ${error.message}</p>`;
            resultsSection.style.display = 'block';
        } finally {
            uploadBtn.disabled = false;
            uploadBtn.textContent = 'Upload & Analyze';
        }
    }
    
    function displayResults(result) {
        let html = '<h3>✅ Analysis Complete</h3>';
        
        if (result.rows) {
            html += `<p><strong>Rows:</strong> ${result.rows}</p>`;
        }
        
        if (result.columns) {
            html += `<p><strong>Columns:</strong> ${result.columns.join(', ')}</p>`;
        }
        
        if (result.summary) {
            html += '<h4>Statistical Summary</h4>';
            html += '<pre>' + JSON.stringify(result.summary, null, 2) + '</pre>';
        }
        
        if (result.predictions) {
            html += '<h4>Predictions</h4>';
            html += '<pre>' + JSON.stringify(result.predictions, null, 2) + '</pre>';
        }
        
        resultsContent.innerHTML = html;
        resultsSection.style.display = 'block';
        resultsContent.scrollIntoView({ behavior: 'smooth' });
    }
});

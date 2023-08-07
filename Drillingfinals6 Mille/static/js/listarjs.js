let dataTable;
let dataTableIsInitialized = false;

(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el curso?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();

const dataTableOptionsX = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7] },
        // { orderable: false, targets: [5, 6] },     // sea ordenable o no
        // { searchable: false, targets: [5, 6] } // sea buscable o no
    ],
    pageLength: 5,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listAutos();

    dataTable = $('#datatable-autos').DataTable(dataTableOptionsX);

    dataTableIsInitialized = true;
    };

const listAutos = async () => {
    try{
        const response=await fetch("http://127.0.0.1:8000/list_autos/")
        const data = await response.json();
        console.log(data.autos);

        let content='';
        data.autos.forEach((auto, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${auto.marca}</td>
                    <td>${auto.modelo}</td>
                    <td>${auto.serialCarroceria}</td>
                    <td>${auto.serialMotor}</td>
                    <td>${auto.categoria}</td>
                    <td>${auto.precio.toLocaleString()}</td>
                    <td>${auto.precio <= 10000
                        ? "<i>bajo</i>"
                        : (auto.precio <= 30000
                            ? "<i>medio</i>"
                            : "<i>alto</i>")
                    }
                    </td>
                </tr>
            `;
        });
        tableBody_autos.innerHTML = content;
    } catch (ex) {
        alert(ex);
    } 
};

window.addEventListener('load', async () => {
    await initDataTable();
});

import React, { Component} from 'react'
import axios from 'axios';

export default class RequestFile extends Component {
    constructor(props) {
        super(props);
        this.state = {
            file: null,
        };
    }
    handleFileChange = (event) => {
        this.setState({ file: event.target.files[0] });
    };

    handleUpload = async () => {
        const formData = new FormData();
        formData.append('csv_file', this.state.file);

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/data/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log(response.data);
        } catch (error) {
            console.error('Error al cargar el archivo:', error);
        }
    };
    render() {
        return (
            <div className='container'>
                <div className="row">
                <div className="col">
                    <label htmlFor="formFile" className="form-label">Seleccione un archivo para ver los sentimientos de cada texto. *Solo csv
                    </label>
                    <input className="form-control" accept='.csv' type="file" id="formFile" onChange={this.handleFileChange}/>
                </div>
                <div className="col-sm-3">
                    <div className="row">
                        <div className='col-8 col-sm-6'>
                            <button className='btn btn-primary' type="button" onClick={this.handleUpload}>Procesar</button>
                        </div>
                    </div>
                </div>
                </div>
            </div>
        )
    }
}

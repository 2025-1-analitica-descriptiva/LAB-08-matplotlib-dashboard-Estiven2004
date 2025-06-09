# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Create docs directory if it doesn't exist
    if not os.path.exists('docs'):
        os.makedirs('docs')
    
    # Read the data
    df = pd.read_csv('files/input/shipping-data.csv')
      # Set style for better looking plots
    plt.style.use('default')
    
    # 1. Shipping per Warehouse Block
    plt.figure(figsize=(10, 6))
    warehouse_counts = df['Warehouse_block'].value_counts()
    plt.bar(warehouse_counts.index, warehouse_counts.values, color='skyblue', edgecolor='black')
    plt.title('Shipping per Warehouse Block', fontsize=16, fontweight='bold')
    plt.xlabel('Warehouse Block', fontsize=12)
    plt.ylabel('Number of Shipments', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/shipping_per_warehouse.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Mode of Shipment
    plt.figure(figsize=(10, 6))
    mode_counts = df['Mode_of_Shipment'].value_counts()
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    plt.pie(mode_counts.values, labels=mode_counts.index, autopct='%1.1f%%', 
            colors=colors, startangle=90, explode=(0.05, 0.05, 0.05))
    plt.title('Mode of Shipment Distribution', fontsize=16, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('docs/mode_of_shipment.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Average Customer Rating
    plt.figure(figsize=(10, 6))
    rating_counts = df['Customer_rating'].value_counts().sort_index()
    plt.bar(rating_counts.index, rating_counts.values, color='lightcoral', edgecolor='black')
    plt.title('Customer Rating Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Customer Rating', fontsize=12)
    plt.ylabel('Number of Customers', fontsize=12)
    plt.xticks(range(1, 6))
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/average_customer_rating.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Weight Distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df['Weight_in_gms'], bins=30, color='lightgreen', alpha=0.7, edgecolor='black')
    plt.title('Weight Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Weight (grams)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/weight_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Create HTML dashboard
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shipping Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 30px;
            }
            .dashboard {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
            }
            .chart-container {
                text-align: center;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #fafafa;
            }
            .chart-container img {
                max-width: 100%;
                height: auto;
                border-radius: 5px;
            }
            .chart-title {
                font-weight: bold;
                margin-bottom: 10px;
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Shipping Data Dashboard</h1>
            <div class="dashboard">
                <div class="chart-container">
                    <div class="chart-title">Shipping per Warehouse Block</div>
                    <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse Block">
                </div>
                <div class="chart-container">
                    <div class="chart-title">Mode of Shipment Distribution</div>
                    <img src="mode_of_shipment.png" alt="Mode of Shipment">
                </div>
                <div class="chart-container">
                    <div class="chart-title">Customer Rating Distribution</div>
                    <img src="average_customer_rating.png" alt="Customer Rating">
                </div>
                <div class="chart-container">
                    <div class="chart-title">Weight Distribution</div>
                    <img src="weight_distribution.png" alt="Weight Distribution">
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Write HTML file
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

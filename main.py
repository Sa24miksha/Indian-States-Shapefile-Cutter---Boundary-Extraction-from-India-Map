import geopandas as gpd
import matplotlib.pyplot as plt
import os

def extract_all_state_boundaries(shapefile_path, state_column, output_directory):
    # Read the shapefile
    india_gdf = gpd.read_file(shapefile_path)

    # Print column names to verify the correct column name
    print("Available columns:", india_gdf.columns)

    # Check unique values in the state column
    print("Available states:", india_gdf[state_column].unique())

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Loop through each unique state in the shapefile
    for state_name in india_gdf[state_column].unique():
        # Filter the GeoDataFrame for the current state
        state_gdf = india_gdf[india_gdf[state_column] == state_name]

        # Plot the state boundary
        state_gdf.plot()
        plt.title(f'Boundary of {state_name}')
        plt.show()

        # Define the output shapefile path
        output_shapefile = os.path.join(output_directory, f'{state_name}_boundary.shp')

        # Save the state's boundary to a new shapefile
        state_gdf.to_file(output_shapefile)
        print(f"Extracted state boundary saved to '{output_shapefile}'")

# Specify the path to the input shapefile
shapefile_path = r"C:\Users\Hii\Downloads\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India_State_Boundary.shp"  

# Specify the name of the column containing state names
state_column = 'State_Name' 

# Specify the output directory to save individual state shapefiles
output_directory = r"C:\Users\Hii\Downloads\sam\cutting indian state from shape file\output"

# Call the function to extract and save boundaries for all states
extract_all_state_boundaries(shapefile_path, state_column, output_directory)




# can also be done as :


#1 import geopandas as gpd
# import matplotlib.pyplot as plt


# def extract_state_boundary(shapefile_path, state_column, state_name):
 
#     india_gdf = gpd.read_file(shapefile_path)

    
#     print(india_gdf.head())

    
#     state_gdf = india_gdf[india_gdf[state_column] == state_name]

    
#     if state_gdf.empty:
#         print(f"State '{state_name}' not found in the shapefile.")
#         return

    
#     state_gdf.plot()
#     plt.title(f'Boundary of {state_name}')
#     plt.show()

    
#     output_shapefile = f'{state_name}_boundary.shp'
#     state_gdf.to_file(output_shapefile)
#     print(f"Extracted state boundary saved to '{output_shapefile}'")


# shapefile_path = r"C:\Users\Hii\Downloads\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India_State_Boundary.shp"  
# state_column = 'State_Name' 
# state_name = 'Chhattisgarh'  

# extract_state_boundary(shapefile_path, state_column, state_name)







# #2
# import geopandas as gpd
# import matplotlib.pyplot as plt
# import os

# def extract_all_state_boundaries(shapefile_path, state_column, output_directory):
#     # Read the shapefile
#     india_gdf = gpd.read_file(shapefile_path)

#     # Create the output directory if it doesn't exist
#     os.makedirs(output_directory, exist_ok=True)

#     # Loop through each unique state in the shapefile
#     for state_name in india_gdf[state_column].unique():
#         # Filter the GeoDataFrame for the current state
#         state_gdf = india_gdf[india_gdf[state_column] == state_name]

#         # Plot the state boundary
#         state_gdf.plot()
#         plt.title(f'Boundary of {state_name}')
#         plt.show()

#         # Define the output shapefile path
#         output_shapefile = os.path.join(output_directory, f'{state_name}_boundary.shp')

#         # Save the state's boundary to a new shapefile
#         state_gdf.to_file(output_shapefile)
#         print(f"Extracted state boundary saved to '{output_shapefile}'")

# # Specify the path to the input shapefile
# shapefile_path = r"C:\Users\Hii\Downloads\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India_State_Boundary.shp"  

# # Specify the name of the column containing state names
# state_column = 'State_Name' 

# # Specify the output directory to save individual state shapefiles
# output_directory = r"C:\Users\Hii\Downloads\sam\cutting indian state from shape file\output"

# # Call the function to extract and save boundaries for all states
# extract_all_state_boundaries(shapefile_path, state_column, output_directory)








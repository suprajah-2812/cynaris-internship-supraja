import pandas as pd
import os


# Load the CSV dataset into a Pandas DataFrame
df = pd.read_csv("week1_numpy/aiml_training_data.csv")

# Print the shape of the DataFrame
print("Shape:")
print(df.shape)

# Print the data types of each column
print("\nData Types:")
print(df.dtypes)

# Print the first 10 rows
print("\nFirst 10 Rows:")
print(df.head(10))

# Filter rows where booking status is completed
completed_bookings = df[df["status"] == "completed"]

print("\nCompleted Bookings:")
print(completed_bookings.head(10))

# Group bookings by service type and count them
service_counts = df.groupby("service_type")["booking_id"].count()

print("\nBookings by Service Type:")
print(service_counts)


# Create a second DataFrame with service department information
service_info = pd.DataFrame({
    "service_type": [
        "AC Repair",
        "Carpentry",
        "Deep Cleaning",
        "Electrician",
        "Painting",
        "Pest Control",
        "Plumbing",
        "Salon at Home"
    ],
    "department": [
        "Technical",
        "Home Improvement",
        "Cleaning",
        "Technical",
        "Home Improvement",
        "Cleaning",
        "Technical",
        "Beauty"
    ]
})

# Merge the original DataFrame with the service information
merged_df = pd.merge(df, service_info, on="service_type", how="left")

print("\nMerged DataFrame:")
print(merged_df.head(10))

# Create a pivot table showing booking counts by city and service type
booking_pivot = pd.pivot_table(
    df,
    index="city",
    columns="service_type",
    values="booking_id",
    aggfunc="count",
    fill_value=0
)

print("\nBooking Pivot Table:")
print(booking_pivot)

# Export the DataFrame to CSV
df.to_csv("week1_numpy/cleaned_bookings.csv", index=False)

print("\nCSV file exported successfully.")

# Export the DataFrame to Parquet
df.to_parquet("week1_numpy/cleaned_bookings.parquet", index=False)

print("Parquet file exported successfully.")


# Compare the sizes of the exported CSV and Parquet files
csv_size = os.path.getsize("week1_numpy/cleaned_bookings.csv")
parquet_size = os.path.getsize("week1_numpy/cleaned_bookings.parquet")

print("\nFile Size Comparison:")
print(f"CSV: {csv_size} bytes")
print(f"Parquet: {parquet_size} bytes")
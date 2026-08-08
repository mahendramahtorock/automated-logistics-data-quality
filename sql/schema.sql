CREATE TABLE shipments (
    shipment_id VARCHAR(30),
    container_id VARCHAR(30),
    carrier VARCHAR(100),
    origin VARCHAR(100),
    destination VARCHAR(100),
    origin_country VARCHAR(5),
    destination_country VARCHAR(5),
    shipment_date DATE,
    expected_arrival DATE,
    actual_arrival DATE,
    status VARCHAR(30),
    actual_transit_days INTEGER,
    expected_transit_days INTEGER
);

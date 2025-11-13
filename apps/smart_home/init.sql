-- Create schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS smarthome;

-- Create the sensors table
CREATE TABLE IF NOT EXISTS smarthome.sensors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    value FLOAT DEFAULT 0,
    unit VARCHAR(20),
    status VARCHAR(20) NOT NULL DEFAULT 'inactive',
    last_updated TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Create indexes for common queries
CREATE INDEX IF NOT EXISTS idx_sensors_type ON smarthome.sensors(type);
CREATE INDEX IF NOT EXISTS idx_sensors_location ON smarthome.sensors(location);
CREATE INDEX IF NOT EXISTS idx_sensors_status ON smarthome.sensors(status);

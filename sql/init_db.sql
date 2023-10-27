------------ SCHEMA: site ------------ 
--Delete schema
DROP SCHEMA IF EXISTS site CASCADE;
--Create schema
CREATE SCHEMA IF NOT EXISTS site;


-- Delete table site
DROP TABLE IF EXISTS site.site CASCADE;

-- Create table site
CREATE TABLE IF NOT EXISTS site.site (
	site_id           SERIAL       PRIMARY KEY,
	homepage_data_id  INT          UNIQUE NOT NULL,
	homepage_id       INT          UNIQUE NOT NULL,
	full_url          VARCHAR      NULL,
	endpoint_path     VARCHAR      NULL,
	protocol          VARCHAR      NULL,
	params            VARCHAR[]    NULL,
	page_extension    VARCHAR(10)  NULL,
	port              INT          NULL,
	tl_domain         VARCHAR      NULL,
	sub_domains       VARCHAR[]    NULL,
	date_updated      DATE         DEFAULT CURRENT_DATE
);


------------ SCHEMA: page_data ------------
--Delete schema
DROP SCHEMA IF EXISTS page_data CASCADE;
--Create schema
CREATE SCHEMA IF NOT EXISTS page_data;

-- Delete table page
DROP TABLE IF EXISTS page_data.page CASCADE;

-- Create table page
CREATE TABLE IF NOT EXISTS page_data.page (
	page_id          SERIAL       PRIMARY KEY,
	page_data_id     INT          UNIQUE NOT NULL,
	site_id          INT          UNIQUE NOT NULL,
	full_url         VARCHAR      NULL,
	endpoint_path    VARCHAR      NULL,
	protocol         VARCHAR      NULL,
	params           VARCHAR[]    NULL,
	page_extension   VARCHAR(10)  NULL,
	port             INT          NULL,
	tl_domain        VARCHAR      NULL,
	sub_domains      VARCHAR[]    NULL,
	homepage         BOOLEAN      NOT NULL,
	date_updated     DATE         DEFAULT CURRENT_DATE
);


-- Delete table page_data
DROP TABLE IF EXISTS page_data.page_data CASCADE;

-- Create table page_data.page_data
CREATE TABLE IF NOT EXISTS page_data.page_data (
	page_data_id     SERIAL       PRIMARY KEY,
	page_id          INT          UNIQUE NOT NULL,
	site_id          INT          UNIQUE NOT NULL,
	comments         VARCHAR[]    NULL,
	js_code          TEXT         NULL,
	js_urls          VARCHAR[]    NULL,
	page_extension   VARCHAR(10)  NULL,
	params           VARCHAR[]    NULL,
	urls             VARCHAR[]    NULL,
	date_updated     DATE         DEFAULT CURRENT_DATE
	post_resp        VARCHAR      NULL,
	get_resp         VARCHAR      NULL,
	options_resp     VARCHAR      NULL,
	put_resp         VARCHAR      NULL,
	patch_resp       VARCHAR      NULL,
	head_resp        VARCHAR      NULL
);


-- Add foreign key constraints to site.site
ALTER TABLE site.site
ADD FOREIGN KEY (homepage_data_id) REFERENCES page_data.page_data(page_data_id) ON DELETE CASCADE;

ALTER TABLE site.site
ADD FOREIGN KEY (homepage_id) REFERENCES page_data.page(page_id) ON DELETE CASCADE;

-- Add unique indexes to site.site
CREATE UNIQUE INDEX site_id on site.site (site_id, homepage_data_id, homepage_id);

-- Add foreign key constraints to page_data.page
ALTER TABLE page_data.page
ADD FOREIGN KEY (page_data_id) REFERENCES page_data.page_data(page_id) ON DELETE CASCADE;

ALTER TABLE page_data.page
ADD FOREIGN KEY (site_id) REFERENCES site.site(site_id);

-- Add unique indexes to page_data.page
CREATE UNIQUE INDEX page_id on page_data.page (page_id, page_data_id, site_id);

-- Add foreign key constraints to page_data.page_data
ALTER TABLE page_data.page_data
ADD FOREIGN KEY (page_id) REFERENCES page_data.page(page_id);

ALTER TABLE page_data.page_data
ADD FOREIGN KEY (site_id) REFERENCES site.site(site_id);

-- Add unique indexes to page_data.page_data
CREATE UNIQUE INDEX page_data_id on page_data.page_data (page_data_id, page_id, site_id);

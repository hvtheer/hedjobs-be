-- Insert data using a CASE statement to determine matching rates
INSERT INTO rate_career_matching (career_id1, career_id2, matching_rate, created_at, updated_at)
SELECT 
    c1.career_id AS career_id1,
    c2.career_id AS career_id2,
    CASE
        WHEN c1.career_id = c2.career_id THEN 1.00 -- Perfect match for same career
        -- Software Development
        WHEN c1.career_id IN (1,2,3,4,5,6,39,80,81,82) AND c2.career_id IN (1,2,3,4,5,6,39,80,81,82) THEN 0.90
        -- Data Science and Analytics
        WHEN c1.career_id IN (12,13,14,15,16,17,53,54,63,64) AND c2.career_id IN (12,13,14,15,16,17,53,54,63,64) THEN 0.85
        -- DevOps and Cloud
        WHEN c1.career_id IN (7,8,35,36,73,74,75,76,77,78) AND c2.career_id IN (7,8,35,36,73,74,75,76,77,78) THEN 0.85
        -- Cybersecurity
        WHEN c1.career_id IN (18,19,20,50,60,61,62,86,97) AND c2.career_id IN (18,19,20,50,60,61,62,86,97) THEN 0.85
        -- Network and Systems
        WHEN c1.career_id IN (9,10,11,55,56,57,58,59) AND c2.career_id IN (9,10,11,55,56,57,58,59) THEN 0.80
        -- Project Management and Leadership
        WHEN c1.career_id IN (21,22,23,48,49,50,73) AND c2.career_id IN (21,22,23,48,49,50,73) THEN 0.75
        -- Design and User Experience
        WHEN c1.career_id IN (24,25,87,90,91) AND c2.career_id IN (24,25,87,90,91) THEN 0.80
        -- Quality Assurance and Testing
        WHEN c1.career_id IN (26,27,51) AND c2.career_id IN (26,27,51) THEN 0.85
        -- Emerging Technologies
        WHEN c1.career_id IN (37,38,42,43,44,45,83,84,85) AND c2.career_id IN (37,38,42,43,44,45,83,84,85) THEN 0.80
        -- AI and Machine Learning
        WHEN c1.career_id IN (13,14,40,41,64) AND c2.career_id IN (13,14,40,41,64) THEN 0.90
        -- IT Support and Operations
        WHEN c1.career_id IN (29,30,31,79) AND c2.career_id IN (29,30,31,79) THEN 0.75
        -- Business and IT Alignment
        WHEN c1.career_id IN (32,33,34,46,47,66,67,68) AND c2.career_id IN (32,33,34,46,47,66,67,68) THEN 0.70
        -- Digital Marketing and Growth
        WHEN c1.career_id IN (69,70,71,72) AND c2.career_id IN (69,70,71,72) THEN 0.75
        -- Hardware and Low-level Programming
        WHEN c1.career_id IN (93,94,95) AND c2.career_id IN (93,94,95) THEN 0.85
        -- Trending Careers (adjust as needed)
        WHEN c1.career_id IN (5,7,8,12,13,14,18,19,35,36,37,42,43,44,85) AND c2.career_id IN (5,7,8,12,13,14,18,19,35,36,37,42,43,44,85) THEN 0.85
        -- Software Development with Data Science
        WHEN (c1.career_id IN (1,2,3,4,5,6) AND c2.career_id IN (12,13,14,15,16,17)) OR
             (c2.career_id IN (1,2,3,4,5,6) AND c1.career_id IN (12,13,14,15,16,17)) THEN 0.75
        -- DevOps with Cybersecurity
        WHEN (c1.career_id IN (7,8,35,36) AND c2.career_id IN (18,19,20,50,60,61,62)) OR
             (c2.career_id IN (7,8,35,36) AND c1.career_id IN (18,19,20,50,60,61,62)) THEN 0.80
        -- AI/ML with Software Development
        WHEN (c1.career_id IN (13,14,40,41) AND c2.career_id IN (1,2,3,4,5,6)) OR
             (c2.career_id IN (13,14,40,41) AND c1.career_id IN (1,2,3,4,5,6)) THEN 0.80
        ELSE 0.50 -- Default lower matching rate for less related careers
    END AS matching_rate,
    NOW() AS created_at,
    NOW() AS updated_at
FROM 
    (SELECT DISTINCT career_id FROM (VALUES 
        (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),
        (21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),
        (41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),(53),(54),(55),(56),(57),(58),(59),(60),
        (61),(62),(63),(64),(65),(66),(67),(68),(69),(70),(71),(72),(73),(74),(75),(76),(77),(78),(79),(80),
        (81),(82),(83),(84),(85),(86),(87),(88),(89),(90),(91),(92),(93),(94),(95),(96),(97),(98),(99),(100)
    ) AS c(career_id)) c1
CROSS JOIN
    (SELECT DISTINCT career_id FROM (VALUES 
        (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),
        (21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),
        (41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),(53),(54),(55),(56),(57),(58),(59),(60),
        (61),(62),(63),(64),(65),(66),(67),(68),(69),(70),(71),(72),(73),(74),(75),(76),(77),(78),(79),(80),
        (81),(82),(83),(84),(85),(86),(87),(88),(89),(90),(91),(92),(93),(94),(95),(96),(97),(98),(99),(100)
    ) AS c(career_id)) c2
WHERE c1.career_id <= c2.career_id; -- This ensures we don't duplicate pairs



-- Insert data using a CASE statement to determine matching rates
INSERT INTO rate_skill_matching (skill_id1, skill_id2, matching_rate, created_at, updated_at)
SELECT 
    s1.skill_id AS skill_id1,
    s2.skill_id AS skill_id2,
    CASE
        WHEN s1.skill_id = s2.skill_id THEN 1.00 -- Perfect match for same skill
        -- Frontend Web Development
        WHEN s1.skill_id IN (1,2,3,4,5,6,7) AND s2.skill_id IN (1,2,3,4,5,6,7) THEN 0.90
        -- Backend Web Development
        WHEN s1.skill_id IN (8,9,10,11,12,13,14,15,16) AND s2.skill_id IN (8,9,10,11,12,13,14,15,16) THEN 0.85
        -- Programming Languages
        WHEN s1.skill_id IN (3,4,16,17,18,19,20,21,22,23,24,25,26) AND s2.skill_id IN (3,4,16,17,18,19,20,21,22,23,24,25,26) THEN 0.80
        -- Databases
        WHEN s1.skill_id IN (27,28,29,30,31,32,33,34,35) AND s2.skill_id IN (27,28,29,30,31,32,33,34,35) THEN 0.85
        -- DevOps and Cloud
        WHEN s1.skill_id IN (37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53) AND s2.skill_id IN (37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53) THEN 0.80
        -- Operating Systems and Scripting
        WHEN s1.skill_id IN (54,55,56,57,58) AND s2.skill_id IN (54,55,56,57,58) THEN 0.75
        -- Project Management and Collaboration
        WHEN s1.skill_id IN (59,60,61,62,63,64) AND s2.skill_id IN (59,60,61,62,63,64) THEN 0.70
        -- Data Science and Machine Learning
        WHEN s1.skill_id IN (65,66,67,68,69,70,71,72,73,74,75,76) AND s2.skill_id IN (65,66,67,68,69,70,71,72,73,74,75,76) THEN 0.90
        -- Big Data
        WHEN s1.skill_id IN (77,78,79,80,81,82,83) AND s2.skill_id IN (77,78,79,80,81,82,83) THEN 0.85
        -- Cybersecurity
        WHEN s1.skill_id IN (85,86,87,88,89,90,91,92) AND s2.skill_id IN (85,86,87,88,89,90,91,92) THEN 0.85
        -- IoT and Embedded Systems
        WHEN s1.skill_id IN (93,94,95,96,97,98,99,100) AND s2.skill_id IN (93,94,95,96,97,98,99,100) THEN 0.80
        -- Trending Skills (adjust as needed)
        WHEN s1.skill_id IN (5,7,17,24,25,30,37,38,39,40,41,65,66,67,68,84,85) AND s2.skill_id IN (5,7,17,24,25,30,37,38,39,40,41,65,66,67,68,84,85) THEN 0.85
        -- Frontend with Backend
        WHEN (s1.skill_id IN (1,2,3,4,5,6,7) AND s2.skill_id IN (8,9,10,11,12,13,14,15,16)) OR
             (s2.skill_id IN (1,2,3,4,5,6,7) AND s1.skill_id IN (8,9,10,11,12,13,14,15,16)) THEN 0.75
        -- Programming Languages with Databases
        WHEN (s1.skill_id IN (3,4,16,17,18,19,20,21,22,23,24,25,26) AND s2.skill_id IN (27,28,29,30,31,32,33,34,35)) OR
             (s2.skill_id IN (3,4,16,17,18,19,20,21,22,23,24,25,26) AND s1.skill_id IN (27,28,29,30,31,32,33,34,35)) THEN 0.70
        -- DevOps with Programming Languages
        WHEN (s1.skill_id IN (37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53) AND s2.skill_id IN (3,4,16,17,18,19,20,21,22,23,24,25,26)) OR
             (s2.skill_id IN (37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53) AND s1.skill_id IN (3,4,16,17,18,19,20,21,22,23,24,25,26)) THEN 0.75
        ELSE 0.50 -- Default lower matching rate for less related skills
    END AS matching_rate,
    NOW() AS created_at,
    NOW() AS updated_at
FROM 
    (SELECT DISTINCT skill_id FROM (VALUES 
        (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),
        (21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),
        (41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),(53),(54),(55),(56),(57),(58),(59),(60),
        (61),(62),(63),(64),(65),(66),(67),(68),(69),(70),(71),(72),(73),(74),(75),(76),(77),(78),(79),(80),
        (81),(82),(83),(84),(85),(86),(87),(88),(89),(90),(91),(92),(93),(94),(95),(96),(97),(98),(99),(100)
    ) AS s(skill_id)) s1
CROSS JOIN
    (SELECT DISTINCT skill_id FROM (VALUES 
        (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),
        (21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),
        (41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),(53),(54),(55),(56),(57),(58),(59),(60),
        (61),(62),(63),(64),(65),(66),(67),(68),(69),(70),(71),(72),(73),(74),(75),(76),(77),(78),(79),(80),
        (81),(82),(83),(84),(85),(86),(87),(88),(89),(90),(91),(92),(93),(94),(95),(96),(97),(98),(99),(100)
    ) AS s(skill_id)) s2
WHERE s1.skill_id <= s2.skill_id; -- This ensures we don't duplicate pairs



-- Create the rate_certificate_matching table if it doesn't exist
CREATE TABLE IF NOT EXISTS rate_certificate_matching (
    certificate_id1 INT,
    certificate_id2 INT,
    matching_rate DECIMAL(3,2),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    PRIMARY KEY (certificate_id1, certificate_id2)
);

-- Insert data using a CASE statement to determine matching rates
INSERT INTO rate_certificate_matching (certificate_id1, certificate_id2, matching_rate, created_at, updated_at)
SELECT 
    c1.certificate_id AS certificate_id1,
    c2.certificate_id AS certificate_id2,
    CASE
        WHEN c1.certificate_id = c2.certificate_id THEN 1.00 -- Perfect match for same certificate
        -- Japanese Language Certificates
        WHEN c1.certificate_id IN (1,2,3,4,5,6,7,8) AND c2.certificate_id IN (1,2,3,4,5,6,7,8) THEN 0.90
        -- English Language Certificates
        WHEN c1.certificate_id IN (9,10,11,12,13,14,15,16) AND c2.certificate_id IN (9,10,11,12,13,14,15,16) THEN 0.90
        -- Cloud Certifications
        WHEN c1.certificate_id IN (17,18,19,20,21,22,23,24,25,26,27,28) AND c2.certificate_id IN (17,18,19,20,21,22,23,24,25,26,27,28) THEN 0.85
        -- Security Certifications
        WHEN c1.certificate_id IN (29,30,31,36,50,51,52,53,54,55,56) AND c2.certificate_id IN (29,30,31,36,50,51,52,53,54,55,56) THEN 0.80
        -- Networking Certifications
        WHEN c1.certificate_id IN (32,33,34,35,58,59,60) AND c2.certificate_id IN (32,33,34,35,58,59,60) THEN 0.75
        -- Project Management and Agile Certifications
        WHEN c1.certificate_id IN (38,39,40,63,64,65,66) AND c2.certificate_id IN (38,39,40,63,64,65,66) THEN 0.70
        -- Database Certifications
        WHEN c1.certificate_id IN (41,42,67,68) AND c2.certificate_id IN (41,42,67,68) THEN 0.80
        -- Data Science and Analytics Certifications
        WHEN c1.certificate_id IN (43,44,77,78,79,80,81) AND c2.certificate_id IN (43,44,77,78,79,80,81) THEN 0.85
        -- DevOps and Container Certifications
        WHEN c1.certificate_id IN (45,46,47,48) AND c2.certificate_id IN (45,46,47,48) THEN 0.75
        -- Blockchain Certifications
        WHEN c1.certificate_id IN (71,72,73) AND c2.certificate_id IN (71,72,73) THEN 0.90
        -- Privacy Certifications
        WHEN c1.certificate_id IN (74,75) AND c2.certificate_id IN (74,75) THEN 0.85
        -- Software Development and Quality Assurance Certifications
        WHEN c1.certificate_id IN (92,93,94,95,96) AND c2.certificate_id IN (92,93,94,95,96) THEN 0.75
        -- IT Service Management Certifications
        WHEN c1.certificate_id IN (37,85,86) AND c2.certificate_id IN (37,85,86) THEN 0.70
        -- Business Analysis and Process Improvement Certifications
        WHEN c1.certificate_id IN (87,88,89,90,91) AND c2.certificate_id IN (87,88,89,90,91) THEN 0.65
        -- Language Certifications (Japanese or English) with IT Certifications
        WHEN (c1.certificate_id IN (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16) AND c2.certificate_id NOT IN (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
             OR (c2.certificate_id IN (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16) AND c1.certificate_id NOT IN (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
        THEN 0.50
        ELSE 0.40 -- Lower matching rate for certificates with less overlap
    END AS matching_rate,
    NOW() AS created_at,
    NOW() AS updated_at
FROM 
    (SELECT DISTINCT certificate_id FROM (VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),(21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),(41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),(53),(54),(55),(56),(57),(58),(59),(60),(61),(62),(63),(64),(65),(66),(67),(68),(69),(70),(71),(72),(73),(74),(75),(76),(77),(78),(79),(80),(81),(82),(83),(84),(85),(86),(87),(88),(89),(90),(91),(92),(93),(94),(95),(96),(97),(98),(99),(100)) AS c(certificate_id)) c1
CROSS JOIN
    (SELECT DISTINCT certificate_id FROM (VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),(21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),(41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),(53),(54),(55),(56),(57),(58),(59),(60),(61),(62),(63),(64),(65),(66),(67),(68),(69),(70),(71),(72),(73),(74),(75),(76),(77),(78),(79),(80),(81),(82),(83),(84),(85),(86),(87),(88),(89),(90),(91),(92),(93),(94),(95),(96),(97),(98),(99),(100)) AS c(certificate_id)) c2
WHERE c1.certificate_id <= c2.certificate_id; -- This ensures we don't duplicate pairs


-- Insert data using a CASE statement to determine matching rates
INSERT INTO rate_city_matching (city_id1, city_id2, matching_rate, created_at, updated_at)
SELECT 
    c1.city_id AS city_id1,
    c2.city_id AS city_id2,
    CASE
        WHEN c1.city_id = c2.city_id THEN 1.00 -- Perfect match for same city
        -- Major cities in Vietnam
        WHEN c1.city_id IN (1,2,3,4,5) AND c2.city_id IN (1,2,3,4,5) THEN 0.90
        -- Major cities in Japan
        WHEN c1.city_id IN (76,90,86) AND c2.city_id IN (76,90,86) THEN 0.90
        -- Cities within the same country (Vietnam)
        WHEN c1.city_id BETWEEN 1 AND 63 AND c2.city_id BETWEEN 1 AND 63 THEN 0.70
        -- Cities within the same country (Japan)
        WHEN c1.city_id BETWEEN 64 AND 110 AND c2.city_id BETWEEN 64 AND 110 THEN 0.70
        -- Northern Vietnam cities
        WHEN c1.city_id IN (1,3,8,9,11,18,25,26,27,28,30,31,37,38,40,41,42,44,54,55,56,60,62,63) 
             AND c2.city_id IN (1,3,8,9,11,18,25,26,27,28,30,31,37,38,40,41,42,44,54,55,56,60,62,63) THEN 0.75
        -- Southern Vietnam cities
        WHEN c1.city_id IN (2,5,6,7,10,12,14,15,16,17,22,23,29,32,33,39,43,51,58,59,61) 
             AND c2.city_id IN (2,5,6,7,10,12,14,15,16,17,22,23,29,32,33,39,43,51,58,59,61) THEN 0.75
        -- Central Vietnam cities
        WHEN c1.city_id IN (4,13,19,20,21,24,34,35,36,45,46,47,48,49,50,52,53,57) 
             AND c2.city_id IN (4,13,19,20,21,24,34,35,36,45,46,47,48,49,50,52,53,57) THEN 0.75
        -- Kanto region cities in Japan
        WHEN c1.city_id IN (71,72,73,74,75,76,77,82) AND c2.city_id IN (71,72,73,74,75,76,77,82) THEN 0.80
        -- Kansai region cities in Japan
        WHEN c1.city_id IN (88,89,90,91,92,93) AND c2.city_id IN (88,89,90,91,92,93) THEN 0.80
        -- Hokkaido and Tohoku region cities in Japan
        WHEN c1.city_id BETWEEN 64 AND 70 AND c2.city_id BETWEEN 64 AND 70 THEN 0.75
        -- Chubu region cities in Japan
        WHEN c1.city_id IN (78,79,80,81,83,84,85,86,87) AND c2.city_id IN (78,79,80,81,83,84,85,86,87) THEN 0.75
        -- Chugoku region cities in Japan
        WHEN c1.city_id BETWEEN 94 AND 98 AND c2.city_id BETWEEN 94 AND 98 THEN 0.75
        -- Shikoku region cities in Japan
        WHEN c1.city_id BETWEEN 99 AND 102 AND c2.city_id BETWEEN 99 AND 102 THEN 0.75
        -- Kyushu and Okinawa region cities in Japan
        WHEN c1.city_id BETWEEN 103 AND 110 AND c2.city_id BETWEEN 103 AND 110 THEN 0.75
        -- Cities from different countries (Vietnam and Japan)
        ELSE 0.40
    END AS matching_rate,
    NOW() AS created_at,
    NOW() AS updated_at
FROM 
    (SELECT DISTINCT city_id FROM (VALUES 
        (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),
        (21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),
        (41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),(53),(54),(55),(56),(57),(58),(59),(60),
        (61),(62),(63),(64),(65),(66),(67),(68),(69),(70),(71),(72),(73),(74),(75),(76),(77),(78),(79),(80),
        (81),(82),(83),(84),(85),(86),(87),(88),(89),(90),(91),(92),(93),(94),(95),(96),(97),(98),(99),(100),
        (101),(102),(103),(104),(105),(106),(107),(108),(109),(110)
    ) AS c(city_id)) c1
CROSS JOIN
    (SELECT DISTINCT city_id FROM (VALUES 
        (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),
        (21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),
        (41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),(53),(54),(55),(56),(57),(58),(59),(60),
        (61),(62),(63),(64),(65),(66),(67),(68),(69),(70),(71),(72),(73),(74),(75),(76),(77),(78),(79),(80),
        (81),(82),(83),(84),(85),(86),(87),(88),(89),(90),(91),(92),(93),(94),(95),(96),(97),(98),(99),(100),
        (101),(102),(103),(104),(105),(106),(107),(108),(109),(110)
    ) AS c(city_id)) c2
WHERE c1.city_id <= c2.city_id; -- This ensures we don't duplicate pairs

-- S script that creates a view need_meeting that lists
-- l students that have a score under 80 (strict)
-- n no last_meeting or more than 1 month.
CREATE VIEW need_meeting AS SELECT name from students WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));

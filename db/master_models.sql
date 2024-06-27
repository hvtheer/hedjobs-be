-- Insert dummy data into m_skill
INSERT INTO m_skill (skill_id, skill_name, lang_code, created_at, updated_at)
VALUES
    (1, 'Java', 'en', NOW(), NOW()),
    (2, 'Python', 'en', NOW(), NOW()),
    (3, 'C++', 'en', NOW(), NOW()),
    (4, 'JavaScript', 'en', NOW(), NOW()),
    (5, 'SQL', 'en', NOW(), NOW()),
    (6, 'HTML/CSS', 'en', NOW(), NOW()),
    (7, 'PHP', 'en', NOW(), NOW()),
    (8, 'Ruby', 'en', NOW(), NOW()),
    (9, 'Swift', 'en', NOW(), NOW()),
    (10, 'React', 'en', NOW(), NOW()),
    (1, 'ジャワ', 'ja', NOW(), NOW()),
    (2, 'パイソン', 'ja', NOW(), NOW()),
    (3, 'C++', 'ja', NOW(), NOW()),
    (4, 'JavaScript', 'ja', NOW(), NOW()),
    (5, 'SQL', 'ja', NOW(), NOW()),
    (6, 'HTML/CSS', 'ja', NOW(), NOW()),
    (7, 'PHP', 'ja', NOW(), NOW()),
    (8, 'ルビー', 'ja', NOW(), NOW()),
    (9, 'スウィフト', 'ja', NOW(), NOW()),
    (10, 'リアクト', 'ja', NOW(), NOW()),
    (1, 'Java', 'vi', NOW(), NOW()),
    (2, 'Python', 'vi', NOW(), NOW()),
    (3, 'C++', 'vi', NOW(), NOW()),
    (4, 'JavaScript', 'vi', NOW(), NOW()),
    (5, 'SQL', 'vi', NOW(), NOW()),
    (6, 'HTML/CSS', 'vi', NOW(), NOW()),
    (7, 'PHP', 'vi', NOW(), NOW()),
    (8, 'Ruby', 'vi', NOW(), NOW()),
    (9, 'Swift', 'vi', NOW(), NOW()),
    (10, 'React', 'vi', NOW(), NOW());

-- Insert dummy data into m_position
INSERT INTO m_position (rank_id, rank_name, lang_code, created_at, updated_at)
VALUES
    (1, 'Intern', 'en', NOW(), NOW()),
    (2, 'Junior Developer', 'en', NOW(), NOW()),
    (3, 'Senior Developer', 'en', NOW(), NOW()),
    (4, 'Project Manager', 'en', NOW(), NOW()),
    (5, 'Quality Assurance', 'en', NOW(), NOW()),
    (6, 'Technical Lead', 'en', NOW(), NOW()),
    (1, 'インターン', 'ja', NOW(), NOW()),
    (2, 'ジュニアデベロッパー', 'ja', NOW(), NOW()),
    (3, 'シニアデベロッパー', 'ja', NOW(), NOW()),
    (4, 'プロジェクトマネージャー', 'ja', NOW(), NOW()),
    (5, '品質保証', 'ja', NOW(), NOW()),
    (6, 'テクニカルリード', 'ja', NOW(), NOW()),
    (1, 'Thực tập sinh', 'vi', NOW(), NOW()),
    (2, 'Lập trình viên mới', 'vi', NOW(), NOW()),
    (3, 'Lập trình viên chính', 'vi', NOW(), NOW()),
    (4, 'Quản lý dự án', 'vi', NOW(), NOW()),
    (5, 'Đảm bảo chất lượng', 'vi', NOW(), NOW()),
    (6, 'Trưởng nhóm kỹ thuật', 'vi', NOW(), NOW());

-- Insert dummy data into m_certificate
INSERT INTO m_certificate (certificate_id, certificate_name, lang_code, created_at, updated_at)
VALUES
    (1, 'TOEIC', 'en', NOW(), NOW()),
    (2, 'JLPT', 'en', NOW(), NOW()),
    (3, 'IELTS', 'en', NOW(), NOW()),
    (4, 'TOEFL', 'en', NOW(), NOW()),
    (5, 'PMP', 'en', NOW(), NOW()),
    (6, 'CCNA', 'en', NOW(), NOW()),
    (7, 'CompTIA', 'en', NOW(), NOW()),
    (8, 'AWS Certified', 'en', NOW(), NOW()),
    (1, 'TOEIC', 'ja', NOW(), NOW()),
    (2, 'JLPT', 'ja', NOW(), NOW()),
    (3, 'IELTS', 'ja', NOW(), NOW()),
    (4, 'TOEFL', 'ja', NOW(), NOW()),
    (5, 'PMP', 'ja', NOW(), NOW()),
    (6, 'CCNA', 'ja', NOW(), NOW()),
    (7, 'CompTIA', 'ja', NOW(), NOW()),
    (8, 'AWS 認定', 'ja', NOW(), NOW()),
    (1, 'TOEIC', 'vi', NOW(), NOW()),
    (2, 'JLPT', 'vi', NOW(), NOW()),
    (3, 'IELTS', 'vi', NOW(), NOW()),
    (4, 'TOEFL', 'vi', NOW(), NOW()),
    (5, 'PMP', 'vi', NOW(), NOW()),
    (6, 'CCNA', 'vi', NOW(), NOW()),
    (7, 'CompTIA', 'vi', NOW(), NOW()),
    (8, 'AWS Certified', 'vi', NOW(), NOW());

-- Insert dummy data into m_career
INSERT INTO m_career (career_id, career_name, lang_code, created_at, updated_at)
VALUES
    (1, 'Software Engineer', 'en', NOW(), NOW()),
    (2, 'Business Analyst', 'en', NOW(), NOW()),
    (3, 'Data Scientist', 'en', NOW(), NOW()),
    (4, 'System Administrator', 'en', NOW(), NOW()),
    (5, 'Network Engineer', 'en', NOW(), NOW()),
    (6, 'UI/UX Designer', 'en', NOW(), NOW()),
    (1, 'ソフトウェアエンジニア', 'ja', NOW(), NOW()),
    (2, 'ビジネスアナリスト', 'ja', NOW(), NOW()),
    (3, 'データサイエンティスト', 'ja', NOW(), NOW()),
    (4, 'システム管理者', 'ja', NOW(), NOW()),
    (5, 'ネットワークエンジニア', 'ja', NOW(), NOW()),
    (6, 'UI/UX デザイナー', 'ja', NOW(), NOW()),
    (1, 'Kỹ sư phần mềm', 'vi', NOW(), NOW()),
    (2, 'Chuyên viên phân tích kinh doanh', 'vi', NOW(), NOW()),
    (3, 'Nhà khoa học dữ liệu', 'vi', NOW(), NOW()),
    (4, 'Quản trị hệ thống', 'vi', NOW(), NOW()),
    (5, 'Kỹ sư mạng', 'vi', NOW(), NOW()),
    (6, 'Thiết kế UI/UX', 'vi', NOW(), NOW());

-- Insert dummy data into m_education
INSERT INTO m_education (education_id, education_name, lang_code, created_at, updated_at)
VALUES
    (1, 'Diploma', 'en', NOW(), NOW()),
    (2, 'Bachelor Degree', 'en', NOW(), NOW()),
    (3, 'Master Degree', 'en', NOW(), NOW()),
    (4, 'PhD', 'en', NOW(), NOW()),
    (1, 'ディプロマ', 'ja', NOW(), NOW()),
    (2, '学士号', 'ja', NOW(), NOW()),
    (3, '修士号', 'ja', NOW(), NOW()),
    (4, '博士号', 'ja', NOW(), NOW()),
    (1, 'Bằng Cao đẳng', 'vi', NOW(), NOW()),
    (2, 'Bằng Đại học', 'vi', NOW(), NOW()),
    (3, 'Thạc sĩ', 'vi', NOW(), NOW()),
    (4, 'Tiến sĩ', 'vi', NOW(), NOW());

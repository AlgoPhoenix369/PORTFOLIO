-- Portfolio Database Schema for Supabase/PostgreSQL
-- Run this script to create all necessary tables

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Profiles table
CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    title VARCHAR(200) NOT NULL,
    location VARCHAR(200),
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20),
    summary TEXT,
    github_url VARCHAR(200),
    linkedin_url VARCHAR(200),
    portfolio_url VARCHAR(200),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Experiences table
CREATE TABLE IF NOT EXISTS experiences (
    id SERIAL PRIMARY KEY,
    company VARCHAR(100) NOT NULL,
    position VARCHAR(200) NOT NULL,
    location VARCHAR(200),
    start_date VARCHAR(20),
    end_date VARCHAR(20),
    is_current BOOLEAN DEFAULT FALSE,
    description TEXT,
    responsibilities JSONB DEFAULT '[]',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Educations table
CREATE TABLE IF NOT EXISTS educations (
    id SERIAL PRIMARY KEY,
    institution VARCHAR(200) NOT NULL,
    degree VARCHAR(200) NOT NULL,
    field_of_study VARCHAR(200),
    location VARCHAR(200),
    start_date VARCHAR(20),
    end_date VARCHAR(20),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Skills table
CREATE TABLE IF NOT EXISTS skills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    proficiency_level INTEGER CHECK (proficiency_level >= 1 AND proficiency_level <= 100),
    years_of_experience INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    technologies JSONB DEFAULT '[]',
    duration VARCHAR(50),
    role VARCHAR(100),
    features JSONB DEFAULT '[]',
    project_url VARCHAR(200),
    github_url VARCHAR(200),
    image_url VARCHAR(200),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Certifications table
CREATE TABLE IF NOT EXISTS certifications (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    issuer VARCHAR(200) NOT NULL,
    issue_date VARCHAR(20),
    expiry_date VARCHAR(20),
    credential_id VARCHAR(100),
    credential_url VARCHAR(200),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Awards table
CREATE TABLE IF NOT EXISTS awards (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    organization VARCHAR(200) NOT NULL,
    year VARCHAR(20),
    scope VARCHAR(50),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Contact Messages table
CREATE TABLE IF NOT EXISTS contact_messages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    subject VARCHAR(200),
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_experiences_start_date ON experiences(start_date DESC);
CREATE INDEX IF NOT EXISTS idx_educations_end_date ON educations(end_date DESC);
CREATE INDEX IF NOT EXISTS idx_skills_category ON skills(category);
CREATE INDEX IF NOT EXISTS idx_projects_created_at ON projects(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_certifications_issue_date ON certifications(issue_date DESC);
CREATE INDEX IF NOT EXISTS idx_awards_year ON awards(year DESC);
CREATE INDEX IF NOT EXISTS idx_contact_messages_created_at ON contact_messages(created_at DESC);

-- Create function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for updated_at
CREATE TRIGGER update_profiles_updated_at BEFORE UPDATE ON profiles
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_experiences_updated_at BEFORE UPDATE ON experiences
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_educations_updated_at BEFORE UPDATE ON educations
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_skills_updated_at BEFORE UPDATE ON skills
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_projects_updated_at BEFORE UPDATE ON projects
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_certifications_updated_at BEFORE UPDATE ON certifications
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_awards_updated_at BEFORE UPDATE ON awards
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Insert sample data (from Babajide Salami's CV)
-- Profile
INSERT INTO profiles (name, title, location, email, phone, summary, github_url, linkedin_url)
VALUES (
    'Babajide Salami',
    'AI Training Specialist & Software Engineer',
    'Croydon, England, United Kingdom',
    'babajide.salami@email.com',
    '+44 7XXX XXXXXX',
    'Results-driven AI Training Specialist and Software Engineer with extensive experience in RLHF (Reinforcement Learning from Human Feedback), LLM evaluation, and data annotation for cutting-edge AI systems. Proven expertise in Python, NLP, and machine learning workflows with a strong background in content quality assurance and remote collaboration.',
    'https://github.com/PhoenixAlgo369',
    'https://linkedin.com/in/babajide-salami-'
);

-- Experiences (sample)
INSERT INTO experiences (company, position, location, start_date, end_date, is_current, description, responsibilities)
VALUES 
('SNORKEL AI', 'Expert Contributor (Gauss HLE Project)', 'Remote', 'Dec 2025', 'Feb 2026', false, 
 'Contributed to the Gauss HLE (High-Level Evaluation) project, providing expert-level annotations for complex reasoning tasks and advanced NLP benchmarks.',
 '["Collaborated with research teams to develop and refine evaluation methodologies for large language model capabilities", "Delivered high-quality labeled datasets with exceptional inter-annotator agreement scores", "Provided detailed feedback on model outputs to identify failure modes and improvement opportunities"]'),

('TELUS INTERNATIONAL', 'Senior AI Trainer & Responsible AI Maker', 'Remote', 'Jun 2025', 'Jan 2026', false,
 'Led AI training initiatives for major tech clients, specializing in content moderation, safety evaluation, and bias detection in language models.',
 '["Developed comprehensive guidelines and training materials for junior annotators", "Conducted rigorous quality audits on annotated datasets, achieving high accuracy standards", "Collaborated with cross-functional teams to implement responsible AI practices"]'),

('NEXUS AI SOLUTIONS', 'AI Training Specialist (Contract)', 'Remote', 'Mar 2022', 'Present', true,
 'Designed and executed comprehensive data annotation projects for computer vision and natural language processing applications.',
 '["Implemented quality control processes that significantly improved annotation accuracy", "Trained and mentored teams of freelance annotators", "Developed custom annotation guidelines for specialized domains including healthcare, finance, and legal"]');

-- Skills (sample)
INSERT INTO skills (name, category, proficiency_level, years_of_experience)
VALUES 
-- AI & Data Training
('RLHF', 'AI & Data Training', 95, 3),
('LLM Fine-tuning', 'AI & Data Training', 90, 2),
('Data Annotation', 'AI & Data Training', 95, 4),
('Prompt Engineering', 'AI & Data Training', 92, 3),
('Model Evaluation', 'AI & Data Training', 90, 3),
('Quality Assurance', 'AI & Data Training', 95, 5),

-- Languages & Frameworks
('Python', 'Languages & Frameworks', 95, 5),
('JavaScript', 'Languages & Frameworks', 85, 4),
('TensorFlow', 'Languages & Frameworks', 88, 3),
('PyTorch', 'Languages & Frameworks', 85, 3),
('Scikit-learn', 'Languages & Frameworks', 90, 4),
('Pandas', 'Languages & Frameworks', 92, 4),
('NumPy', 'Languages & Frameworks', 90, 4),
('NLTK', 'Languages & Frameworks', 85, 3),
('spaCy', 'Languages & Frameworks', 88, 3),
('Transformers (Hugging Face)', 'Languages & Frameworks', 90, 2),

-- DevOps & Infrastructure
('Git', 'DevOps & Infrastructure', 90, 5),
('Docker', 'DevOps & Infrastructure', 85, 3),
('AWS (EC2, S3, SageMaker)', 'DevOps & Infrastructure', 88, 3),
('Google Cloud Platform', 'DevOps & Infrastructure', 85, 2),
('CI/CD Pipelines', 'DevOps & Infrastructure', 82, 3),
('RESTful APIs', 'DevOps & Infrastructure', 90, 4),

-- Tools & Platforms
('Jupyter Notebook', 'Tools & Platforms', 95, 5),
('VS Code', 'Tools & Platforms', 92, 4),
('Label Studio', 'Tools & Platforms', 90, 3),
('Prodigy', 'Tools & Platforms', 85, 2),
('Amazon Mechanical Turk', 'Tools & Platforms', 88, 3),
('Snorkel', 'Tools & Platforms', 87, 2),
('Weights & Biases', 'Tools & Platforms', 85, 2),
('MLflow', 'Tools & Platforms', 83, 2);

-- Projects (sample)
INSERT INTO projects (title, description, technologies, duration, role, features)
VALUES 
('Multi-Lingual Sentiment Analysis Platform', 
 'Developed an end-to-end sentiment analysis system capable of processing text in multiple languages with high accuracy.',
 '["Python", "TensorFlow", "spaCy", "FastAPI"]',
 '6 months',
 'Lead Developer',
 '["Multi-language support (English, French, Spanish, German, Yoruba)", "Real-time inference API with <100ms response time", "Custom preprocessing pipelines for text normalization", "Achieved 92% accuracy on test datasets"]'),

('Automated Data Annotation Pipeline',
 'Built an automated data labeling pipeline using weak supervision techniques to reduce manual annotation effort.',
 '["Python", "Snorkel", "Label Studio", "Docker"]',
 '4 months',
 'ML Engineer',
 '["70% reduction in manual annotation time", "Weak supervision labeling functions", "Integration with Label Studio and Prodigy", "Quality metrics dashboard"]'),

('LLM Evaluation Framework',
 'Created a comprehensive evaluation framework for benchmarking large language model performance across multiple tasks.',
 '["Python", "Hugging Face Transformers", "Weights & Biases"]',
 '3 months',
 'Research Engineer',
 '["Standardized evaluation metrics for LLMs", "Automated benchmarking across 15+ tasks", "Interactive dashboards with W&B integration", "Safety and bias evaluation modules"]');

-- Education (sample)
INSERT INTO educations (institution, degree, field_of_study, location, start_date, end_date, description)
VALUES 
('University of Edinburgh', 'PhD in Computational Linguistics & AI', 'Computational Linguistics', 'UK', '2018', '2024', 'Doctoral research in computational linguistics and artificial intelligence'),
('Stanford University', 'MSc in Data Science & Machine Learning', 'Data Science', 'USA', '2015', '2017', 'Master''s degree focusing on machine learning and data science'),
('King''s College London', 'BA in Communications & Linguistics', 'Communications', 'UK', '2010', '2014', 'Bachelor''s degree in communications and linguistics'),
('Moringa School (Kenya)', 'Full Stack Software Development', 'Software Development', 'Kenya/Remote', '2022', '2022', 'Intensive bootcamp in full stack web development'),
('Harvard College (Online)', 'Certificate in Computer Science', 'Computer Science', 'USA', '2020', '2020', 'CS50 - Introduction to Computer Science');

-- Certifications (sample)
INSERT INTO certifications (name, issuer, issue_date, expiry_date)
VALUES 
('AWS Certified Machine Learning - Specialty', 'Amazon Web Services', '2024', NULL),
('Google Cloud Professional Data Engineer', 'Google Cloud', '2023', NULL),
('TensorFlow Developer Certificate', 'Google', '2023', NULL),
('Deep Learning Specialization', 'DeepLearning.AI (Coursera)', '2022', NULL),
('Natural Language Processing Specialization', 'DeepLearning.AI', '2022', NULL),
('Responsible AI Principles', 'Google Cloud', '2023', NULL);

-- Awards (sample)
INSERT INTO awards (title, organization, year, scope, description)
VALUES 
('Outstanding Contributor Award', 'TELUS International AI Community', '2025', 'Global', 'Excellence in AI Training'),
('Best Research Paper', 'ACL Conference on Computational Linguistics', '2023', 'International', 'NLP Research'),
('Academic Excellence Scholarship', 'University of Edinburgh School of Informatics', '2018 - 2024', 'UK', 'PhD Studies');

-- Row Level Security (RLS) Policies for Supabase
-- Enable RLS
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE experiences ENABLE ROW LEVEL SECURITY;
ALTER TABLE educations ENABLE ROW LEVEL SECURITY;
ALTER TABLE skills ENABLE ROW LEVEL SECURITY;
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;
ALTER TABLE certifications ENABLE ROW LEVEL SECURITY;
ALTER TABLE awards ENABLE ROW LEVEL SECURITY;
ALTER TABLE contact_messages ENABLE ROW LEVEL SECURITY;

-- Allow public read access to portfolio data
CREATE POLICY "Allow public read access to profiles" ON profiles
    FOR SELECT USING (true);

CREATE POLICY "Allow public read access to experiences" ON experiences
    FOR SELECT USING (true);

CREATE POLICY "Allow public read access to educations" ON educations
    FOR SELECT USING (true);

CREATE POLICY "Allow public read access to skills" ON skills
    FOR SELECT USING (true);

CREATE POLICY "Allow public read access to projects" ON projects
    FOR SELECT USING (true);

CREATE POLICY "Allow public read access to certifications" ON certifications
    FOR SELECT USING (true);

CREATE POLICY "Allow public read access to awards" ON awards
    FOR SELECT USING (true);

-- Allow public to submit contact messages
CREATE POLICY "Allow public to insert contact messages" ON contact_messages
    FOR INSERT WITH CHECK (true);

-- Only allow authenticated users to read contact messages
CREATE POLICY "Allow authenticated users to read contact messages" ON contact_messages
    FOR SELECT USING (auth.role() = 'authenticated');

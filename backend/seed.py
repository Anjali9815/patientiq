import asyncio
from datetime import date, datetime
from database import AsyncSessionLocal
from models import User, UserHealthProfile, UserInsurancePlan, SymptomEntry, Document, Bill, BillLineItem, ConsentForm



async def seed():
    async with AsyncSessionLocal() as session:
        user1 = User(
            email="test@patientiq.com",
            name="Test User",
            clerk_id="clerk_test_123",
            timezone="America/New_York"
        )
        user2 = User(
            email="jane@patientiq.com",
            name="Jane Smith",
            clerk_id="clerk_jane",
            timezone="America/Chicago"
        )
        session.add_all([user1, user2])
        await session.commit()
        print("User created!")

        hp1 = UserHealthProfile(
            user_id=user1.id,
            age=35,
            biological_sex="Male",
            blood_type="O+",
            chronic_conditions="Hypertension",
            current_medications="Lisinopril",
            allergies="Penicillin",
            past_surgeries="Appendectomy",
            primary_physician="Dr. Adams",
            emergency_contact_name="Mary Doe",
            emergency_contact_phone="555-111-1111"
        )

        hp2 = UserHealthProfile(
            user_id=user2.id,
            age=29,
            biological_sex="Female",
            blood_type="A+",
            chronic_conditions="None",
            current_medications="None",
            allergies="Peanuts",
            past_surgeries="None",
            primary_physician="Dr. Smith",
            emergency_contact_name="John Smith",
            emergency_contact_phone="555-222-2222"
        )

        session.add_all([hp1, hp2])

        # Insurance Plans
        plan1 = UserInsurancePlan(
            user_id=user1.id,
            plan_name="Gold PPO",
            insurer_name="Blue Cross",
            member_id="M12345",
            group_number="G100",
            plan_type="PPO",
            deductible_total=1500,
            deductible_met=600,
            out_of_pocket_max=6000,
            out_of_pocket_met=1200,
            coverage_start=date(2026,1,1),
            coverage_end=date(2026,12,31),
            is_primary=True
        )

        plan2 = UserInsurancePlan(
            user_id=user2.id,
            plan_name="Silver HMO",
            insurer_name="Aetna",
            member_id="M67890",
            group_number="G200",
            plan_type="HMO",
            deductible_total=1000,
            deductible_met=200,
            out_of_pocket_max=5000,
            out_of_pocket_met=300,
            coverage_start=date(2026,1,1),
            coverage_end=date(2026,12,31),
            is_primary=True
        )

        session.add_all([plan1, plan2])
        await session.flush()


        # Symptom Entries
        symptoms = [

            SymptomEntry(
                user_id=user1.id,
                entry_date=datetime.utcnow(),
                input_type="Manual",
                symptom_tags="Headache",
                severity_score=5,
                duration="2 hours"
            ),

            SymptomEntry(
                user_id=user1.id,
                entry_date=datetime.utcnow(),
                input_type="Manual",
                symptom_tags="Fever",
                severity_score=7,
                duration="1 day"
            ),

            SymptomEntry(
                user_id=user1.id,
                entry_date=datetime.utcnow(),
                input_type="Manual",
                symptom_tags="Back Pain",
                severity_score=4,
                duration="3 days"
            ),
        ]

        session.add_all(symptoms)


        # Documents
        doc1 = Document(
            user_id=user1.id,
            doc_type="Medical Bill",
            file_bucket="patient-docs",
            file_key="bill001.pdf",
            original_filename="bill001.pdf",
            mime_type="application/pdf",
            file_size_bytes=125000,
            page_count=2,
            status="Processed"
        )

        doc2 = Document(
            user_id=user1.id,
            doc_type="Insurance Card",
            file_bucket="patient-docs",
            file_key="insurance.pdf",
            original_filename="insurance.pdf",
            mime_type="application/pdf",
            file_size_bytes=98000,
            page_count=1,
            status="Processed"
        )

        session.add_all([doc1, doc2])
        await session.flush()


        # Bill
        bill = Bill(
            user_id=user1.id,
            document_id=doc1.id,
            insurance_plan_id=plan1.id,
            provider_name="City Hospital",
            total_billed=1500,
            total_allowed=1200,
            total_paid_by_insurance=900,
            patient_responsibility=300,
            amount_paid=0,
            bill_status="Pending",
            service_date_start=date(2026,5,20),
            service_date_end=date(2026,5,20)
        )

        session.add(bill)
        await session.flush()


        # Bill Line Items
        items = [

            BillLineItem(
                bill_id=bill.id,
                cpt_code="99213",
                cpt_description="Office Visit",
                units=1,
                billed_amount=300,
                allowed_amount=250,
                paid_amount=200
            ),

            BillLineItem(
                bill_id=bill.id,
                cpt_code="80050",
                cpt_description="Blood Test",
                units=1,
                billed_amount=500,
                allowed_amount=400,
                paid_amount=350
            ),

            BillLineItem(
                bill_id=bill.id,
                cpt_code="71020",
                cpt_description="Chest X-Ray",
                units=1,
                billed_amount=700,
                allowed_amount=550,
                paid_amount=350
            ),
        ]

        session.add_all(items)

        # Consent Form
        consent = ConsentForm(
            user_id=user1.id,
            document_id=doc2.id,
            procedure_name="Knee Surgery",
            provider_name="City Hospital",
            facility_name="Orthopedic Center",
            procedure_date=date(2026,5,21),
            patient_signed=True,
            decode_status="Completed"
        )

        session.add(consent)

        # Commit
        await session.commit()
        print("Database seeded successfully!")

asyncio.run(seed())



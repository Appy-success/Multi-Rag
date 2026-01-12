# Demo Examples for Contoso Assistant

**Created by:** Aparna Rajawat

---

### Full Demo (10 minutes)
1. **Product Assistant**: "What outdoor gear do you have for camping?"
2. **Product Assistant**: "Show me waterproof tents"
3. **Product Assistant**: "What's the price of the Adventurer Pro Backpack?"


4. **Manual Assistant**: "How do I set up the TrailMaster X4 Tent?"
5. **Manual Assistant**: "What are the dimensions of the tent when packed?"
6. **Manual Assistant**: "Does the Adventurer Pro Backpack have hydration compatibility?"
7. **Product Assistant**: "Do you sell hiking jackets?"
8. **Manual Assistant**: "What sizes are available for the Summit Breeze Jacket?"

### Advanced Demo (15 minutes)
Show multi-turn conversations with context:
1. **Product Assistant**: "Show me camping tents"
2. **Product Assistant**: "Which one is best for 4 people?" (follow-up)
3. **Product Assistant**: "What's the price?" (follow-up)
4. **Manual Assistant**: "Tell me about the TrailMaster X4 Tent setup"
5. **Manual Assistant**: "How long does setup take?" (follow-up)
6. **Manual Assistant**: "What about ventilation?" (follow-up)
7. **Product Assistant**: "Do you have backpacks?"
8. **Manual Assistant**: "How do I adjust the backpack straps?"

---

## 💡 Tips for Effective Demo

1. **Start Simple**: Begin with basic queries to show core functionality
2. **Show Context**: Demonstrate multi-turn conversations where the AI remembers context
3. **Switch Routes**: Alternate between Product and Manual to show different indexes
4. **Highlight RAG**: Explain how the AI searches indexed data for accurate answers
5. **Show Clearing**: Use the "Clear Chat" button to reset between demo sections
6. **Error Handling**: Show what happens with queries that have no results

---

## 📝 Notes
- The Product Assistant searches the `contoso-products` index
- The Manual Assistant searches the `contoso-manuals-index` index
- Both use RAG (Retrieval-Augmented Generation) for accurate, grounded responses
- Chat history is maintained separately for each assistant
